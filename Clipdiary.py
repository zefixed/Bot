
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Test')
#-----------------------------------------------------------------------------------------------------------------------
bot.send_message(message.chat.id, 'Приятно познакомиться ', name)
#-----------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def hello_text(call):
    if call.data == 'want':
        regi = bot.send_message(call.message.chat.id,'Тогда перейдём к регистрации')
        bot.register_next_step_handler(regi, reg_message)
    elif call.data == 'wantnt':
        bot.send_message(call.message.chat.id, 'Ну как хочешь, Аноним')
#-----------------------------------------------------------------------------------------------------------------------
def reg_message(message):
    name = bot.send_message(message.chat.id, 'Как мне к вам обращаться?')
    bot.register_next_step_handler(name, hello_message)
#-----------------------------------------------------------------------------------------------------------------------
keyboard1 = types.InlineKeyboardMarkup()
cbbn1 = types.InlineKeyboardButton(text="Хочу", callback_data="want")
cbbn2 = types.InlineKeyboardButton(text="Не хочу", callback_data="wantnt")
keyboard1.add(cbbn1, cbbn2)
#-----------------------------------------------------------------------------------------------------------------------
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Хочу', 'Не хочу')
#-----------------------------------------------------------------------------------------------------------------------
if message.text.lower == 'хочу':
    bot.register_next_step_handler(reg, reg_message)
elif message.text.lower == 'не хочу':
    bot.send_message(message.chat.id, 'Ну как хочешь, Аноним')
#-----------------------------------------------------------------------------------------------------------------------
def send_text(message):
    try:
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
    except Exception:
        bot.reply_to(message, 'Ошибка')

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------