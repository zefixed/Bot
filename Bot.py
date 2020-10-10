import telebot

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Привет', 'Пока')

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
def hello_message(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Очень приятно, {name}. Рад тебя видеть.'.format(name=message.text), reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет' and name == '':
        bot.send_message(message.chat.id, 'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg')
    elif message.text.lower() == 'привет' and name != '':
        bot.send_message(message.chat.id, 'Привет, {}'.format(name))
    elif message.text.lower() == 'пока' and name == '':
        bot.send_message(message.chat.id, 'Прощай, Аноним')
    elif message.text.lower() == 'пока' and name != '':
        bot.send_message(message.chat.id, 'Прощай, {}'.format(name))


bot.polling()
