import os
import telebot
from telebot import types
import messages
import AiRequests
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
    btn3 = types.KeyboardButton('Gemini')
    btn4 = types.KeyboardButton('Meta')
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

def setX_True():
    global x 
    x = True

def setX_False():
    global x 
    x = False

x = True

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if x == True:
        if message.text == "ChatGPT":
            bot.send_message(message.chat.id, "You selected Option 1!")
        elif message.text == "Copilot":
            bot.send_message(message.chat.id, "You selected Option 2!")
        elif message.text == "Gemini":
            bot.send_message(message.chat.id, "You selected Option 2!")
        elif message.text == "Meta":
            bot.send_message(message.chat.id, "You selected META")
            setX_False()
        elif message.text == "Personalized AI":
            bot.send_message(message.chat.id, "You selected Option 2!")  
        else:
            bot.send_message(message.chat.id, "Choose a option!")      
    else:
        bot.send_message(message.chat.id ,AiRequests.AskGpt(message, "llama3-8b-8192"))




def run():
    bot.polling() 
run()