from flask import Flask, render_template, request
import cloudscraper
from newspaper import Article

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main page with the input form."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Receives form data and renders the results page.
    Shows the scraped article data.
    """
    url = request.form.get('url_input', '').strip()
    text_input = request.form.get('text_input', '').strip()

    article_title = ""
    article_authors = []
    article_text = ""

    # If URL is provided, scrape it
    if url:
        try:
            scraper = cloudscraper.create_scraper()
            html = scraper.get(url).text

            article = Article(url)
            article.download(input_html=html)
            article.parse()

            article_title = article.title
            article_authors = article.authors
            article_text = article.text

        except Exception as e:
            article_title = "Error"
            article_text = f"Error scraping article: {e}"

    # If user pasted text, use it directly
    elif text_input:
        article_title = "User Provided Text"
        article_text = text_input
        article_authors = []

    else:
        article_title = "No Input Provided"
        article_text = "Please enter a URL or paste article text."
        article_authors = []

    # Prepare data for template
    scraped_data = {
        'article_title': article_title,
        'article_authors': article_authors,
        'article_text': article_text[:5000]  # truncate if needed
    }

    return render_template('results.html', results=scraped_data)

if __name__ == '__main__':
    app.run(debug=True)
