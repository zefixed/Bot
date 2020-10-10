
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Test')
#------------------------------------------------------------------
bot.send_message(message.chat.id, 'Приятно познакомиться ', name)