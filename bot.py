import os
import telebot
from telebot import types
import messages
import AiRequests
from Interfaces import IVarHandler, IAiModelHandler
from Requests import GeneratePrompts
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.environ.get("TELEGRAM_API_KEY"), parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    # Create a ReplyKeyboardMarkup
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Add buttons to the menu
    btn1 = types.KeyboardButton('ChatGPT')
    btn2 = types.KeyboardButton('Copilot')
    btn3 = types.KeyboardButton('Gemma AI')
    btn4 = types.KeyboardButton('Meta AI')
    btn5 = types.KeyboardButton('Personalized AI')
    menu.add(btn1, btn2)
    menu.add(btn3, btn4)
    menu.add(btn5)
    # Send a message with the custom menu
    bot.send_message(
        message.chat.id, 
        text=messages.welcome_message, 
        reply_markup=menu,
    )

@bot.message_handler(commands=['stop'])
def start_command(message):
    IVarHandler.VarHandler.handler = True 


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if IVarHandler.VarHandler.handler == True and IVarHandler.VarHandler.promptHandler != True:
        if message.text == "ChatGPT":
            bot.send_message(message.chat.id, "You selected Option 1!")
            IVarHandler.VarHandler.handler = False
        elif message.text == "Copilot":
            bot.send_message(message.chat.id, "You selected Option 2!")
            IVarHandler.VarHandler.handler = False
        elif message.text == "Gemma AI":
            bot.send_message(message.chat.id, "You selected Gemma Ai")
            IAiModelHandler.AiModelHandler.handler = "gemma2-9b-it"
            IVarHandler.VarHandler.handler = False
        elif message.text == "Meta AI":
            bot.send_message(message.chat.id, "You selected Meta AI")
            IAiModelHandler.AiModelHandler.handler = "llama3-8b-8192"
            IVarHandler.VarHandler.handler = False
        elif message.text == "Personalized AI":
            bot.send_message(message.chat.id, "You selected custom AI\nDescribe how you want your chatbot to behave.")
            IVarHandler.VarHandler.promptHandler = True
            IVarHandler.VarHandler.handler = False
            IAiModelHandler.AiModelHandler.handler = "llama3-8b-8192"
        else:
            bot.send_message(message.chat.id, "Choose a option!")      

    elif IVarHandler.VarHandler.handler == False and IVarHandler.VarHandler.promptHandler != True:
        bot.send_message(message.chat.id, AiRequests.AskGpt(message.text, IAiModelHandler.AiModelHandler.handler))

    elif IVarHandler.VarHandler.handler == False and IVarHandler.VarHandler.promptHandler == True:                      #Generating custom prompts
        bot.send_message(message.chat.id, GeneratePrompts.GeneratePrompts(message.text, IAiModelHandler.AiModelHandler.handler))




def run():
    bot.polling() 
run()