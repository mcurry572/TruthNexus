# Group Member Names
Will C, 

# Web GUI Python Starter (FastAPI + Jinja)

A batteries-included starter to build a small web GUI in Python (FastAPI) and connect to your existing web APIs.

## Features
- FastAPI backend with server-side templates (Jinja) and a vanilla JS front-end
- Organized `app/` package with `api_client.py` for talking to your web APIs
- `.env` based config for API base URLs and secrets
- Static assets under `app/static` (CSS/JS)
- Example route that calls an external API through `api_client`

---

## Quick Start (CLI)

1. **Create & activate a virtual environment**
```bash
# Windows (PowerShell)
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Copy env file and set your API base URL**
```bash
cp .env.example .env  # (Windows PowerShell) copy .env.example .env
# edit .env and set API_BASE_URL=https://your-api.example.com
```

4. **Run the server**
```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

---

## Visual Studio 2022 Setup (Windows)

1. Install the **Python development** workload in Visual Studio Installer.
2. **File → Open → Folder...** and select this project folder.
3. VS will detect the Python environment; if not, create a new **virtual environment** from the `requirements.txt` (Solution Explorer → Python Environments → Add).
4. Set the run configuration:
   - **Debug → Add Configuration...** (or in the Python toolbar) set the module to `uvicorn` and arguments to `app.main:app --reload`.
   - Alternate: create a **Python debugging profile** that runs `uvicorn` with the same args.
5. **Start Debugging (F5)** to launch the dev server.
6. Use the built-in terminal for `git` commands.

> Tip: Visual Studio also supports **Tasks** for running/deploying commands; you can create one that runs `uvicorn app.main:app --reload`.

---

## Project Structure

```
webgui-python-starter/
├─ app/
│  ├─ main.py
│  ├─ api_client.py
│  ├─ config.py
│  ├─ templates/
│  │  ├─ base.html
│  │  └─ index.html
│  └─ static/
│     ├─ css/
│     │  └─ style.css
│     └─ js/
│        └─ app.js
├─ tests/
│  └─ test_smoke.py
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## GitHub: First Push

```bash
git init
git add .
git commit -m "Initial commit: FastAPI web GUI starter"
git branch -M main
git remote add origin <YOUR-GITHUB-REPO-URL>
git push -u origin main
```

---

## Where to plug in your APIs

- Put your base URL(s) in `.env`
- Implement API calls in `app/api_client.py`
- Use them in route handlers in `app/main.py`

Check the inline TODOs for the exact spots.