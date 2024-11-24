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

def AskGpt(userMessage, aiModel):                               #method to use in bot to pass the message from the user and return the answer from an AI model
    chat_completion = client.chat.completions.create(
        messages=[
                {
                "role": "user",
                "content": f"{userMessage}",
                }
            ],
        model=aiModel,
        )
    replyMessage = chat_completion.choices[0].message.content
    return replyMessage
