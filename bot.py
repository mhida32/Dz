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
import pyTelegramBotAPI
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
import pyTelegramBotAPI
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

# Задание 6
credit by karpblch
import pyTelegramBotAPI
import requests
from bot_token import TOKEN


@bot.message_handler(commands=["start"])
def echo(message):
    key = telebot.types.InlineKeyboardMarkup()
    lst = []
    for i in range(5):
        lst.append(telebot.types.InlineKeyboardButton(text="i",callback_data=str(i)))
    key.row(*lst)
    bot.send_message(message.chat.id,'Выберай',reply_markup=key)
                       
@bot.callback_query_handler(func= lambda call:True)
def callback(call):
    if random.randint(0,4) == int(call.data):
        bot.send_message(call.message.chat.id, f'Выиграл')
    else:
        bot.send_message(call.message.chat.id, f'Проиграл')

if __name__ == '__main__':
    bot.infinity_polling()


credit by karpblch
