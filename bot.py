# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
credit by karpblch

# Задание 1
import telebot
from bot_token import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, f"{(message.text * 10)} ")


if __name__ == '__main__':
    bot.infinity_polling()
    
credit by karpblch
