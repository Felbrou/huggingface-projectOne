# 🤗 HuggingFace Poem Generator

![Python](https://img.shields.io/badge/Python-3.10-blue)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference_API-yellow)

A simple AI-powered poem generator using HuggingFace's 
Inference API and the OpenAI Python SDK.

## 🎬 Demo

Enter a poem topic: **ocean**

> The waves crash softly on the shore,
> A rhythm ancient, rich with lore...


## ✨ Features

- 🎨 Generate poems on any topic
- 🤖 Powered by Kimi-K2 model via HuggingFace
- 🔐 Secure token management with .env


## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- HuggingFace account + token

### Installation

# 1. Clone the repo
git clone https://github.com/Felbrou/huggingface-projectOne.git
cd huggingface-projectOne

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your token
cp .env.example .env
# Add your HF_TOKEN inside .env


## 💻 Usage

python main.py

# Output:
# 🎨 Enter a poem topic: sea
# 📜 Your Poem:
# The ocean breathes...


## 📁 Project Structure

huggingface-projectOne/
├── main.py           # Main application
├── .env.example      # Token template (safe to share)
├── requirements.txt  # Dependencies
└── README.md         # This file


## 📄 License
MIT License

## 👤 Author
**Felbrou**
- GitHub: [@Felbrou](https://github.com/Felbrou)
