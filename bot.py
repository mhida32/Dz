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
# Игра
import telebot
from copy import deepcopy
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

users_info ={}
# ВНИМАТАЛЬНО ЧИТАЙНЕ ПЕРЕМЕННУЮ 'locations'
locations = {
    '1' : {'text':'Сюда вы пишите свою историю',
           'items': [],'next_move' : {'текст передвижения' : '2'}, 'exchange': {}},
    
    '2' : { 'text': 'Сюда вы пишите свою историю',
           'items': [], 'next_move':{'текст передвижения': '3',
                                                      'текст передвижения': '4',
                                                      'текст передвижения':'5'},'exchange': {}},
    '3' : {'text' : 'Сюда вы пишите свою историю(первая концовка тут типо смерть)',
           'items': [],'next_move' :{},'exchange': {}},

    '4': {'text': 'Сюда вы пишите свою историю(подбор придмета)'', 
          'items': [],'next_move': {'Вернуть назад': '2'}, 'exchange': {'САМ ПРЕДМЕТ': 'золото : 3'}},
    '5': {'text': 'Сюда вы пишите свою историю(выбор куда идти)'',
        'items': [], 'next_move': {'текст передвижения': '2',
                                            'текст передвижения': '7',    
                                            'текст передвижения': '6'}, 'exchange': {}},
    '6': {'text': 'Сюда вы пишите свою историю',
        'items': ['золотой слиток'], 'next_move': {'Вернуться к подземелью': '5'}, 'exchange': {}},
    '7': {'text': 'Сюда вы пишите свою историю(выбор куда идти)',
        'items': ['золото: 2'], 'next_move' : {'текст передвижения': '8',
                                                'текст передвижения': '5'}, 'exchange': {}}, 
    '8': {'text': 'Сюда вы пишите свою историю(выбор куда идти)',
        'items': [], 'next_move': {'текст передвижения' : '9',
                                        'текст передвижения': '7'}, 'exchange': {}},
    '9': {'text': 'Сюда вы пишите свою историю(Победа)',
        'items': [], 'next_move': {'текст передвижения': '8'}, 'exchange': {'золото: 5': 'выход'}}
}
credit by karpblch
def generate_story(user, position):
    txt = locations[position]['text']
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in users_info[user]['loc'][position]['next_move']:
        key_txt = i
        key_data = locations[position]['next_move'][i]
        keyboard.add(telebot.types.InlineKeyboardButton(text=key_txt, callback_data=key_data))
    
    for i in users_info[user]['loc'] [position]['items']:
        key_txt = 'Bзять предмет - ' + i
        key_data = 'item ' + i
        keyboard.add(telebot.types.InlineKeyboardButton(text=key_txt, callback_data=key_data))

    for i in users_info[user]['loc'][position]['exchange']:
        if i in users_info[user]['items'] or (i.startswith('золото: ') and users_info[user]['coins'] >= int(i.replace('золото:', ''))):
            key_txt='обменять предмет '+ i + ' на ' + users_info[user]['loc'][position]['exchange'][i] 
            key_data= 'exchange ' + i
            keyboard.add(telebot.types.InlineKeyboardButton(text=key_txt, callback_data=key_data))   
    return (txt, keyboard)
    
credit by karpblch    
@bot.message_handler(commands=['game'])
def start_game(message):
    users_info[message.from_user.username] = {'cur_pos': '1', 'coins': 0, 'items': [], 'loc': deepcopy(locations)}
    txt, keyboard = generate_story(message.from_user.username, users_info[message.from_user.username]['cur_pos'])
    bot.send_message(message.chat.id, txt, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in locations)
def callback_query(call):
    users_info[call.from_user.username]['cur_pos'] = call.data
    txt, keyboard = generate_story(call.from_user.username, users_info[call.from_user.username]['cur_pos'])
    bot.send_message(call.message.chat.id, txt, reply_markup=keyboard)

credit by karpblch
@bot.callback_query_handler(func=lambda call: call.data.startswith('item '))
def callback_query(call):
    item = call.data.replace('item ', '')
    if item.startswith('золото: '):
        users_info[call.from_user.username]['coins'] += int(item.replace('золото: ',''))
    else:
        users_info[call.from_user.username]['items'].append(item)
    users_info[call.from_user.username]['loc'][users_info[call.from_user.username]['cur_pos']]['items'].remove(item)
    bot.send_message(call.message.chat.id, 'Готово')
    txt, keyboard = generate_story(call.from_user.username, users_info[call.from_user.username]['cur_pos'])
    bot.send_message(call.message.chat.id, txt, reply_markup=keyboard)



credit by karpblch
@bot.callback_query_handler(func=lambda call: call.data.startswith('exchange '))
def callback_query(call):
    item1=call.data.replace('exchange ','')
    item2=users_info[call.from_user.username]['loc'][users_info[call.from_user.username]['cur_pos']]['exchange'][item1]

    if item1.startswith('золото: '):
        users_info[call.from_user.username]['coins'] = int(item1.replace('золото: ',''))
    else:
        users_info[call.from_user.username]['items'].remove(item1)
    if item2.startswith('золото: '):
        users_info[call.from_user.username]['coins'] += int(item2.replace("золото: "))
    else:
        users_info[call.from_user.username]['items'].append(item2)
    users_info[call.from_user.username]['loc'][users_info[call.from_user.username]['cur_pos']]['exchange'].pop(item1)
    
    if item2 == 'выход':
        bot.send_message(call.message.chat.id, 'Tебе удалось пройти квест')
    else:
        bot.send_message(call.message.chat.id, 'Готово')
        txt, keyboard = generate_story(call.from_user.username, users_info[call.from_user.username]['cur_pos'])
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard)


credit by karpblch
if __name__ == '__main__':
    bot.infinity_polling()

credit by karpblch


