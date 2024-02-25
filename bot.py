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
# Задание 3
credit by karpblch
import telebot
import requests
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def echo(message):
    try:
        quest = message.text.split('\n')
        del quest[0]
        bot.send_poll(message.chat.id, message.text.split('\n'),quest)
    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.chat.id, "В вашем сообщении должно быть от 3 до 11 строк")

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

