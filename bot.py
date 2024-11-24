import telebot
from telebot import types
import messages

bot = telebot.TeleBot("7647716410:AAFXo_mKsyZ9dETZh-Dw852jxy8Z5hhHyDs", parse_mode=None)


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


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "ChatGPT":
        bot.send_message(message.chat.id, "You selected Option 1!")
    elif message.text == "Copilot":
        bot.send_message(message.chat.id, "You selected Option 2!")
    elif message.text == "Gemini":
        bot.send_message(message.chat.id, "You selected Option 2!")
    elif message.text == "Meta":
        bot.send_message(message.chat.id, "You selected Option 2!")
    elif message.text == "Personalized AI":
        bot.send_message(message.chat.id, "You selected Option 2!")        
    else:
        bot.send_message(message.chat.id, "Please choose an option.")


def run():
    bot.polling() 
run()

#xd