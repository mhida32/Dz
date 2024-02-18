# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
credit by karpblch

# Задание 1
import pyTelegramBotAPI
from bot_token import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, f"{(message.text * 10)} ")


if __name__ == '__main__':
    bot.infinity_polling()
    
credit by karpblch

# Задание 2
import pyTelegramBotAPI
import random
from bot_token import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: "рандом" in message.text )
def echo(message):
    bot.send_message(message.chat.id, f"Случайное число: {random.randint(0,100)}")
        

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id,message.text)


if __name__ == '__main__':
    bot.infinity_polling()

credit by karpblch

# Задание 4
credit by karpblch
import telebot
import requests
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

    
@bot.message_handler(commands=["coffee"])
def send_cat(message):
    r = requests.get('https://coffee.alexflipnote.dev/random.json')
    url = r.json()['file']
    bot.send_photo(message.chat.id, url)
    

if __name__ == '__main__':
    bot.infinity_polling()
    
credit by karpblch

