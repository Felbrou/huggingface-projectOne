import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

topic = input("🎨 Enter a poem topic: ")

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct-0905",
    messages=[
        {
            "role": "user",
            "content": f"Generate a poem about: {topic}."
        }
    ],
)

print("\n📜 Your Poem:\n")
print(completion.choices[0].message.content)