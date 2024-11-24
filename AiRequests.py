import os
import requests
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

aiModel = "llama3-8b-8192"

userMessage = "TestMessage"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{userMessage}",
        }
    ],
    model=aiModel,
)

print(chat_completion.choices[0].message.content)