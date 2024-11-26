from groq import Groq
from Interfaces.IApiKey import client


def GeneratePrompts(userMessage, aiModel):                               #method to use in bot to pass the message from the user and return the answer from an AI model
    generatePrompts = "Generate accurate prompts (only prompts, no other text) for AI model to behave accordingly to the following text: "
    chat_completion = client.chat.completions.create(
        messages=[
                {
                "role": "user",
                "content": f"{generatePrompts}{userMessage}",
                }
            ],
        model=aiModel,
        )
    generatedPrompts = chat_completion.choices[0].message.content
    return generatedPrompts