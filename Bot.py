import telebot

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, Пользователь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, Пользователь')


bot.polling()
