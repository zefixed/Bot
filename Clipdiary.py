def ------(message):
    try:

    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))
#-----------------------------------------------------------------------------------------------------------------------
bot.send_message(message.chat.id, '')
#-----------------------------------------------------------------------------------------------------------------------
bot.register_next_step_handler(msg, )
#-----------------------------------------------------------------------------------------------------------------------
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
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)

        sql = 'SELECT first_name FROM users WHERE user_id = %s'
        val = (user_id, )
        name = str((cursor.execute(sql, val)))
        print(name)
        bot.send_message(message.chat.id, 'Привет, {}'.format(name))
#-----------------------------------------------------------------------------------------------------------------------
cursor.execute('CREATE TABLE `articles` (`id` tinyint unsigned NOT NULL auto_increment, `question` varchar(255) default NULL, `answer` text, PRIMARY KEY (`id`), FULLTEXT KEY `ft1` (`question`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;')
#-----------------------------------------------------------------------------------------------------------------------
def admin_panel_create_question(message):
    try:
        msg = bot.send_message(message.chat.id, 'Введите вопрос')
        bot.register_next_step_handler(msg, admin_panel_create_answer)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

def admin_panel_create_answer(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_question)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

def admin_panel_create_question(message):
    try:
        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO articles (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, Datab.answer)
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))
#-----------------------------------------------------------------------------------------------------------------------


def admin_panel_create_question(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO radicalpowerlogarithm (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))
#-----------------------------------------------------------------------------------------------------------------------


def admin_panel_delete(message):
    try:
        id = message.text
        sql = 'SELECT * FROM articles WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3(message):
    try:
        id = message.text
        sql = 'DELETE FROM articles WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



