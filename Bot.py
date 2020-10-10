import telebot
from telebot import types

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')


kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

name = ''
i = 0

@bot.message_handler(commands=['start', 'help', 'reg','adm'])
def start_help_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=kb)
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Доступные команду\n'
                                          '1. /start (Используется для начала общения со мной)\n'
                                          '2. /help (Показывает известные мне команды)\n'
                                          '3. /reg (Позволяет мне обращаться к тебе по имени)\n')
    elif message.text == '/reg':
        name = bot.send_message(message.chat.id, 'Как мне к тебе обращаться?')
        bot.register_next_step_handler(name, hello_message)
    elif message.text == '/adm':
        adm = bot.send_message(message.chat.id,'Введите пароль')
        bot.register_next_step_handler(adm, admin_panel)

def hello_message(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Очень приятно, {name}. Рад тебя видеть.'.format(name=message.text), reply_markup=kb)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global name, i
    if message.text.lower() == 'привет' and name == '' and i == 0:
        bot.send_message(message.chat.id, 'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg (не обязательно)')
        i = 1
    elif message.text.lower() == 'привет' and name == '' and i == 1:
        bot.send_message(message.chat.id, 'Привет, Аноним')
        name = 'Аноним'
    elif message.text.lower() == 'привет' and name != '':
        bot.send_message(message.chat.id, 'Привет, {}'.format(name))
    elif message.text.lower() == 'пока' and name == '':
        bot.send_message(message.chat.id, 'Прощай, Аноним')
    elif message.text.lower() == 'пока' and name != '':
        bot.send_message(message.chat.id, 'Прощай, {}'.format(name))

@bot.message_handler(content_types=['text'])
def admin_panel(message):
    if message.text.lower() == 'f297a57a5a743894a0e4a801fc3':
        bot.send_message(message.chat.id, 'Добро пожаловать в админ панель')
        bot.send_message(message.chat.id, 'Здесь пока ничего нет, но скоро я обязательно сяду и что-нибудь сюда добавлю ))')


bot.polling()
