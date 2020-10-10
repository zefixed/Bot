import telebot

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Привет', 'Пока')

@bot.message_handler(commands=['start', 'help', 'reg'])
def start_help_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'В разработке')
    elif message.text == '/reg':
        bot.send_message(message.chat.id, 'В разработке2')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, Пользователь')


bot.polling()
