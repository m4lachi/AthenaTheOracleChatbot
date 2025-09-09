---

# Athena Chatbot 🏛️

A Flask-based web application powered by OpenAI’s API. This chatbot, named **Athena**, embodies the goddess of wisdom and responds to user questions in a concise, myth-inspired style.

---

## ✨ Features

* **Flask Backend** – lightweight and easy-to-deploy web server.
* **OpenAI Integration** – uses the `gpt-4o-mini` model for fast, cost-efficient responses.
* **Custom Persona** – answers as **Athena**, the goddess of wisdom.
* **REST API Endpoint** – `/ask` endpoint accepts JSON input and returns chatbot responses.
* **Simple Frontend** – serves an `index.html` page as the user interface.

---

## 📂 Project Structure

```
├── athenaChatBot.py      # Main Flask application
├── templates/
│   └── index.html       # Frontend interface
├── requirements.txt     # Dependencies
├── .env                 # Environment variables (not committed)
├── .gitignore           # Files/folders to ignore in git
└── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/m4lachi/AthenaTheOracleChatbot.git
cd AthenaTheOracleChatbot
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**Sample `requirements.txt`:**

```
flask>=3.0.0
openai>=1.0.0
python-dotenv>=1.0.0   # For loading .env files
gunicorn>=21.2.0       # Optional: for production deployment
```

---

### 4. Configure OpenAI API Key

#### Option A: Use `.env` file (recommended)

1. Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=your_user_secret_key_here
   ```
2. Add this to **`athenaChatBot.py`** so it loads automatically:

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

#### Option B: Export manually

On macOS/Linux:

```bash
export OPENAI_API_KEY="your_user_secret_key_here"
```

On Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY="your_user_secret_key_here"
```

---

## 🔑 How to Get Your OpenAI User Secret Key

1. **Visit the OpenAI API Keys Page:** [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. **Sign In** with your OpenAI account.
3. **Create a New Secret Key:**

   * Click **"Create new secret key"**.
   * Name your key (e.g., "Athena Chatbot Integration").
   * Select the appropriate permissions (All, Restricted, or Read-Only).
   * Click **"Create secret key"**.
4. **Copy and Store Your Key:** Copy it immediately and keep it secure; you won’t be able to view it again.

**Security Tips:**

* Never share your key publicly.
* Use environment variables (`.env`) for safety.
* Monitor your usage regularly.

For more details, see OpenAI's [API Key Safety Guide](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).

---

## ▶️ Running the App

Start the Flask development server:

```bash
python athenaChatBot.py
```

By default, the app will be available at:

```
http://127.0.0.1:5000
```

---

## 📡 API Usage

### Endpoint: `POST /ask`

**Request body:**

```json
{
  "question": "What is the meaning of wisdom?"
}
```

**Response:**

```json
{
  "answer": "Wisdom is the art of applying knowledge with fairness and foresight, much like the owl that sees in the dark."
}
```

---

## 🌐 Frontend

Open `http://127.0.0.1:5000/` in your browser to use the chatbot via the `index.html` interface.

---

## 🔒 Notes

* Keep your **OpenAI API key** private.
* The app runs in `debug=True` mode for development; disable it for production.

---

## ⚙️ Git Ignore Recommendations

**Sample `.gitignore`:**

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/

# Environment variables
.env

# IDEs
.vscode/
.idea/
```

---

## 🚀 Future Improvements

* Add user authentication.
* Log conversation history.
* Support multiple personas or mythological figures.
* Containerize with Docker for easier deployment.

---
