import telebot
from telebot import types

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Привет', 'Пока')
#keyboard1 = types.InlineKeyboardMarkup()
#cbbn1 = types.InlineKeyboardButton(text="Хочу", callback_data="хочу")
#cbbn2 = types.InlineKeyboardButton(text="Не хочу", callback_data="нехочу")
#keyboard1.add(cbbn1, cbbn2)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Хочу', 'Не хочу')

name = ''

@bot.message_handler(commands=['start', 'help', 'reg'])
def start_help_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'В разработке')
    elif message.text == '/reg':
        name = bot.send_message(message.chat.id, 'Как мне к вам обращаться?')
        bot.register_next_step_handler(name, hello_message)

@bot.message_handler(commands=['reg'])
def reg_message(message):
    name = bot.send_message(message.chat.id, 'Как мне к вам обращаться?')
    bot.register_next_step_handler(name, hello_message)

def hello_message(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Очень приятно, {name}. Рад тебя видеть.'.format(name=message.text), reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет' and name == '':
        reg = bot.send_message(message.chat.id, 'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg', reply_markup=keyboard1)
        if message.text.lower == 'хочу':
            bot.register_next_step_handler(reg, reg_message)
        elif message.text.lower == 'не хочу':
            bot.send_message(message.chat.id, 'Ну как хочешь, Аноним')
    elif message.text.lower() == 'привет' and name != '':
        bot.send_message(message.chat.id, 'Привет, {}'.format(name))
    elif message.text.lower() == 'пока' and name == '':
        bot.send_message(message.chat.id, 'Прощай, Аноним')
    elif message.text.lower() == 'пока' and name != '':
        bot.send_message(message.chat.id, 'Прощай, {}'.format(name))

#@bot.callback_query_handler(func=lambda call: True)
#def hello_text(call):
#    if call.data == 'хочу':


bot.polling()
