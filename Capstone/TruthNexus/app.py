from flask import Flask, render_template, request

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
    This is where you will later integrate your backend analysis logic.
    """
    # You can access the submitted data using request.form
    # url = request.form.get('url_input')
    # text = request.form.get('text_input')
    # For now, we will use placeholder data.

    # --- PLACEHOLDER DATA ---
    # This is the mock data you will replace with your actual analysis results.
    # The structure (dictionary) is designed for easy replacement.
    analysis_results = {
        'score': 82,
        'score_string': "Likely Credible",
        'claims': [
            {
                'claim': "A study in September 2025 found that renewable energy sources have become cheaper than fossil fuels.",
                'evidence': "Placeholder: This claim cross-references with data from the International Renewable Energy Agency (IRENA) reports from 2024 and 2025."
            },
            {
                'claim': "The global adoption of electric vehicles has tripled in the last five years.",
                'evidence': "Placeholder: Verified against sales data from major automotive industry reports."
            },
            {
                'claim': "Policy changes in North America are the primary driver for this shift.",
                'evidence': "Placeholder: This is a point of contention. While policy is a factor, market forces and technological advancements are also significant contributors."
            }
        ],
        'sources': [
            {'source_name': "International Renewable Energy Agency", 'link': '#', 'status': 'Credible'},
            {'source_name': "Global Automotive Market Report 2025", 'link': '#', 'status': 'Credible'},
            {'source_name': "Unverified blog post", 'link': '#', 'status': 'Questionable'}
        ],
        'language_analysis': [
            {'finding': "Use of emotionally charged language detected.", 'example': "'...a disastrous policy that will ruin our economy.'"},
            {'finding': "Presence of sweeping generalizations.", 'example': "'Everyone knows that this is the only solution.'"}
        ]
    }
    # --- END OF PLACEHOLDER DATA ---

    # Render the results page, passing the data to the template
    return render_template('results.html', results=analysis_results)

if __name__ == '__main__':
    app.run(debug=True)