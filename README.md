# 🤗 HuggingFace Poem Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference_API-yellow?logo=huggingface&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple)

> An AI-powered poem generator with a web interface, built using HuggingFace's Inference API, the OpenAI Python SDK, and FastAPI.

---

## 🎬 Demo

```
🎨 Enter a topic: ocean

📜 Your Poem:

The waves crash softly on the shore,
A rhythm ancient, rich with lore,
The sea breathes deep, the tides align,
In every drop, a world divine...
```

---

## ✨ Features

- 🎨 Generate poems on **any topic** via a web interface
- 🤖 Powered by **Kimi-K2 model** via HuggingFace Inference API
- 🌐 **FastAPI web server** with interactive HTML UI
- 🔐 Secure token management with `.env`
- 📄 **Auto-generated API docs** at `/docs` and `/redoc`
- ⚡ Fast async responses with **Uvicorn**

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| Python 3.10+ | Core language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| HuggingFace Inference API | AI model provider |
| OpenAI SDK | API client (pointed to HuggingFace) |
| Jinja2 | HTML templating |
| python-dotenv | Environment variable management |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [HuggingFace account](https://huggingface.co) + API token

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Felbrou/huggingface-projectOne.git
cd huggingface-projectOne

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your token
cp .env.example .env
# Open .env and add your HuggingFace token
```

### ⚙️ Environment Setup

Create a `.env` file based on `.env.example`:

```
HF_TOKEN=your_huggingface_token_here
```

Get your token at 👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 💻 Running the App

### 🌐 Web Interface (FastAPI)

```bash
uvicorn app.api:app --reload
```

Then open your browser at:
```
http://127.0.0.1:8000        ← Web UI
http://127.0.0.1:8000/docs   ← Interactive API docs
http://127.0.0.1:8000/redoc  ← Clean API docs
```

### 🖥️ Command Line (Original Script)

```bash
python main.py
```

---

## 📁 Project Structure

```
huggingface-projectOne/
│
├── app/
│   ├── __init__.py         # Makes app a Python package
│   └── api.py              # FastAPI routes and logic
│
├── templates/
│   └── index.html          # Web UI template
│
├── main.py                 # Original CLI script
├── .env                    # 🔴 Secret tokens (never commit!)
├── .env.example            # ✅ Token template (safe to share)
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
└── README.md               # This file
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Renders the web UI |
| `POST` | `/generate` | Generates a poem from a topic |

---

## 📦 Dependencies

```
openai
python-dotenv
fastapi
uvicorn
jinja2
python-multipart
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🗺️ How It Works

```
Browser → GET /          → FastAPI → renders index.html
User types topic
Browser → POST /generate → FastAPI → HuggingFace API → poem → renders page
```

---

## 🔐 Security Notes

- ✅ Never commit your `.env` file
- ✅ Use `.env.example` to show required variables
- ✅ `.env` and `venv/` are listed in `.gitignore`

---

## 🛣️ Roadmap

- [ ] Add poem style selector (haiku, sonnet, free verse)
- [ ] Save generated poems to a file
- [ ] Compare output from multiple models
- [ ] Deploy to Railway / Render
- [ ] Add poem history/gallery

---

## 📄 License

MIT License — feel free to use and modify!

---

## 👤 Author

**Felbrou**
- GitHub: [@Felbrou](https://github.com/Felbrou)
