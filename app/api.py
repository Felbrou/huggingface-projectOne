import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  # Load environment variables from .env file


# 🚀 Create the FastAPI app
app = FastAPI(title="🤗 Poem Generator")

# 🎨 Tell FastAPI where the HTML files are
templates = Jinja2Templates(directory="templates")

# Initialize HuggingFace client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

# 📌 Route 1 — Home page (GET request)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "poem": None,
    })


# 📌 Route 2 — Generate poem (POST request)
@app.post("/generate", response_class=HTMLResponse)
async def generate_poem(request: Request, topic: str = Form(...)):
    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[
            {
                "role": "user",
                "content": f"Generate a poem about: {topic}."
            }
        ],
    )
    poem = completion.choices[0].message.content

    return templates.TemplateResponse("index.html", {
        "request": request,
        "poem": poem,
        "topic": topic
    })
