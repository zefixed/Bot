import telebot
from telebot import types
import mysql.connector
import config as cfg
import random


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bot_db"
)

cursor = db.cursor()


bot = telebot.TeleBot(cfg.token)

datab_data = {}
user_data = {}
user_data_add = {}  # additional user data
user_data_test = {} # answers to test
s_db = {}           # select table
s_dr = {}           # delete record
test = {}           # [id, question, answer, position]
test_ans = {}       # answers from user
test_ringt_ans = {}
name = ''
question = ''


@bot.message_handler(commands=['start', 'ask', 'help', 'reg', 'rereg', 'info', 'feedback', 'cookie', 'acc_info', 'test', 'shop', 'sdl', 'adm'])
def start_help_message(message):
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=cfg.kb)
        elif message.text == '/ask':
            kb_ask = types.InlineKeyboardMarkup(row_width=1)
            kb_ask1 = types.InlineKeyboardButton(text="Просмотреть список доступных вопросов", callback_data="viev " + str(message.from_user.id) + " ask_start")
            kb_ask2 = types.InlineKeyboardButton(text="Написать вручную", callback_data="write " + str(message.from_user.id) + " ask_start")
            kb_ask.add(kb_ask1, kb_ask2)
            msg = bot.send_message(message.chat.id, 'Вы можете просмотреть список доступных вопросов (не рекомендуется) или задать вопрос вручную', reply_markup=kb_ask)
            bot.register_next_step_handler(msg, callback)
        elif message.text == '/help':
            bot.send_message(message.chat.id, 'Доступные команды\n'
                                              '1. /start (Начало общения)\n'
                                              '2. /ask (Ответы на вопросы)\n'
                                              '3. /help (Доступные команды)\n'
                                              '4. /reg (Регистарция)\n'
                                              '5. /rereg (Перерегистрация)\n'
                                              '6. /info (Информацию о боте)\n'
                                              '7. /feedback (Сообщить об ошибке)\n'
                                              '8. /acc_info (Инфромация об аккаунте)\n'
                                              '9. /test (Тесты)\n'
                                              '10. /shop (Магазин)\n'
                                              '11. /sdl (Расписание)')
        elif message.text == '/reg':
            name = bot.send_message(message.chat.id, 'Введите имя')
            bot.register_next_step_handler(name, reg_firstname_step)
        elif message.text == '/rereg':
            name = bot.send_message(message.chat.id, 'Введите имя')
            bot.register_next_step_handler(name, rereg_firstname_step)
        elif message.text == '/info':
            bot.send_message(message.chat.id, 'Я бот помощник.\n'
                                              'Я был создан для того чтобы помочь тебе в повторении материала по школьным предметам.\n'
                                              'Пока что я могу помочь тебе только по математике 8-11 классов. \n'
                                              'Мои разработчики стараются над введением новых вопросов, если ты хочешь помочь им или нашёл какой-то недочёт в моей работе, пожалуйста, напиши им об этом с помощью /feedback')
        elif message.text == '/feedback':
            kb_fb = types.InlineKeyboardMarkup(row_width=2)
            kb_fb_complaint = types.InlineKeyboardButton(text="Жалоба", callback_data="complaint " + str(message.from_user.id) + " feedback")
            kb_fb_suggestion = types.InlineKeyboardButton(text="Предложение", callback_data="suggestion " + str(message.from_user.id) + " feedback")
            kb_fb.add(kb_fb_complaint, kb_fb_suggestion)
            msg = bot.send_message(message.chat.id, 'О чём вы бы хотели сообщить?', reply_markup=kb_fb)
            bot.register_next_step_handler(msg, callback)
        elif message.text == '/cookie':
            kb_cookie = types.InlineKeyboardMarkup(row_width=2)
            kb_cookie_give = types.InlineKeyboardButton(text="Дать печеньку", callback_data="give " + str(message.from_user.id) + " cookie")
            kb_cookie_exit = types.InlineKeyboardButton(text="Выйти", callback_data="exit " + str(message.from_user.id) + " cookie")
            kb_cookie.add(kb_cookie_give, kb_cookie_exit)
            msg = bot.send_message(message.chat.id, 'Покормить разработчиков', reply_markup=kb_cookie)
            bot.register_next_step_handler(msg, callback)
        elif message.text == '/acc_info':
            bot.send_message(message.chat.id, 'Информация об аккаунте')
            cursor.execute("SELECT * FROM users WHERE user_id = " + str(message.from_user.id) + "")
            i = cursor.fetchall()
            i = i[0]
            bot.send_message(message.chat.id, 'Имя: {}\n'
                                              'Фамилия: {}\n'
                                              'id в боте: {}\n'
                                              'Telegram id: {}\n'
                                              'Деньги: {}₿\n'
                                              'Дата и время первичной регистрации в боте: {}\n'
                                              'Дата и время последней перерегистрации в боте: {}'.format(i[2], i[3], i[0], i[1], float(i[6]), i[4], i[5]))
        elif message.text == '/test':
            kb_test_qty = types.InlineKeyboardMarkup(row_width=4)
            kb_test_qty_2 = types.InlineKeyboardButton(text="2", callback_data="2 " + str(message.from_user.id) + " test_qty")
            kb_test_qty_5 = types.InlineKeyboardButton(text="5", callback_data="5 " + str(message.from_user.id) + " test_qty")
            kb_test_qty_7 = types.InlineKeyboardButton(text="7", callback_data="7 " + str(message.from_user.id) + " test_qty")
            kb_test_qty_10 = types.InlineKeyboardButton(text="10", callback_data="10 " + str(message.from_user.id) + " test_qty")
            kb_test_qty.add(kb_test_qty_2, kb_test_qty_5, kb_test_qty_7, kb_test_qty_10)
            msg = bot.send_message(message.chat.id, 'Из скольки вопросов должен состоять тест?\n(Можете написать своё количество вопросов)', reply_markup=kb_test_qty)
            bot.register_next_step_handler(msg, callback)
        elif message.text == '/shop':
            msg = bot.send_message(message.chat.id, 'В разработке')
            bot.register_next_step_handler(msg, start_help_message)
        elif message.text == '/sdl':
            kb_sdl_cls = types.InlineKeyboardMarkup(row_width=3)
            kb_sdl_cls_3 = types.InlineKeyboardButton(text="3", callback_data="3 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_4 = types.InlineKeyboardButton(text="4", callback_data="4 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_5 = types.InlineKeyboardButton(text="5", callback_data="5 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_6 = types.InlineKeyboardButton(text="6", callback_data="6 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_7 = types.InlineKeyboardButton(text="7", callback_data="7 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_8 = types.InlineKeyboardButton(text="8", callback_data="8 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_9 = types.InlineKeyboardButton(text="9", callback_data="9 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_10 = types.InlineKeyboardButton(text="10", callback_data="10 " + str(message.from_user.id) + " grade")
            kb_sdl_cls_11 = types.InlineKeyboardButton(text="11", callback_data="11 " + str(message.from_user.id) + " grade")
            kb_sdl_cls.add(kb_sdl_cls_9, kb_sdl_cls_10, kb_sdl_cls_11, kb_sdl_cls_6, kb_sdl_cls_7, kb_sdl_cls_8, kb_sdl_cls_3, kb_sdl_cls_4, kb_sdl_cls_5)
            msg = bot.send_message(message.chat.id, 'Выберите класс', reply_markup=kb_sdl_cls)
            bot.register_next_step_handler(msg, callback)
        elif message.text == '/adm':
            msg = bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(msg, admin_panel)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, информация об аккаунте недоступна. Возможная причина ошибки - аккаунт не создан ')


def ask_set_question(message):
    try:
        kb_yes_no = types.InlineKeyboardMarkup(row_width=2)
        kb_yes = types.InlineKeyboardButton(text="Да", callback_data="yes " + str(message.from_user.id) + " ask_except")
        kb_no = types.InlineKeyboardButton(text="Нет", callback_data="no " + str(message.from_user.id) + " ask_except")
        kb_yes_no.add(kb_yes, kb_no)
        question = message.text
        sql = "SELECT answer, edu_mat FROM " + user_data.get(str(message.from_user.id)) + " WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=kb_yes_no)
        bot.register_next_step_handler(msg, callback)
    except Exception as e:
        kb_yes_no = types.InlineKeyboardMarkup(row_width=2)
        kb_yes = types.InlineKeyboardButton(text="Да", callback_data="yes " + str(message.from_user.id) + " ask_except")
        kb_no = types.InlineKeyboardButton(text="Нет", callback_data="no " + str(message.from_user.id) + " ask_except")
        kb_yes_no.add(kb_yes, kb_no)
        msg = bot.send_message(message.chat.id,
                               """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=kb_yes_no)
        bot.register_next_step_handler(msg, callback)
        print(repr(e))


def reg_firstname_step(message):
    try:
        user = ['', '']
        user[0] = message.text
        user_data[message.from_user.id] = user
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, reg_lastname_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def reg_lastname_step(message):
    try:
        user = user_data.get(message.from_user.id)
        user[1] = message.text
        sql = "INSERT INTO users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
        val = (user[0], user[1], message.from_user.id)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, "Вы успешно зарегистрированны!")
        bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def rereg_firstname_step(message):
    try:
        user = ['', '']
        user[0] = message.text
        user_data[message.from_user.id] = user
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, rereg_lastname_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def rereg_lastname_step(message):
    try:
        user = user_data.get(message.from_user.id)
        user[1] = message.text
        sql = 'UPDATE users SET first_name = %s, last_name = %s, rereg = NOW() WHERE user_id = {0}'.format(message.from_user.id)
        val = (user[0], user[1])
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Вы успешно перерегистрированны!")
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def feedback_complaint(message):
    try:
        user_id = message.from_user.id
        problem = message.text

        sql = "INSERT INTO feedback (problem, user_id) VALUES (%s, %s)"
        val = (problem, user_id)
        cursor.execute(sql, val)
        db.commit()

        msg = bot.send_message(message.chat.id, 'Проблема в кротчайшие сроки будет исправлена')
        bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def feedback_suggestion(message):
    try:
        user_id = message.from_user.id
        request = message.text

        sql = "INSERT INTO feedback (request, user_id) VALUES (%s, %s)"
        val = (request, user_id)
        cursor.execute(sql, val)
        db.commit()

        msg= bot.send_message(message.chat.id, 'Мы учтём ваше пожелание')
        bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def test_qty(message):
    try:
        user_data[message.from_user.id] = [message.text, message.text]
        user_data_add[message.from_user.id] = 1
        msg = bot.send_message(message.chat.id, 'По какой теме вы бы хотели проверить свои знания?',reply_markup=cfg.kb_test)
        bot.register_next_step_handler(msg, test_table)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def test_table(message):
    try:
        datab_data[message.from_user.id] = message.text
        if message.text == 'Математика':
            datab_data[message.from_user.id] = 'math'
        elif message.text == 'Физика':
            datab_data[message.from_user.id] = 'phys'
        elif message.text == 'Информатика':
            datab_data[message.from_user.id] = 'inf'
        if message.text != 'Выход':
            cursor.execute('SELECT id, question, answer FROM ' + datab_data[message.from_user.id] + '')
            rows = cursor.fetchall()
            test[message.from_user.id] = r.sample(rows, int(user_data.get(message.from_user.id)[0]))
            ques = [[]] * int(user_data.get(message.from_user.id)[0])
            i = 0
            for que in test[message.from_user.id]:
                q = [0, '', '']
                q[0] = que[0]
                q[1] = que[1]
                q[2] = que[2]
                ques[i] = q
                i += 1
            i = 0
            for que in ques:
                q = [0, '', '', 0]
                q[0] = que[0]
                l = len(que[1])
                q[1] = que[1][0:l // 2]
                q[2] = que[2]
                q[3] = r.randint(1, 4)
                ques[i] = q
                i += 1
            test[message.from_user.id] = ques
            msg = bot.send_message(message.chat.id, 'Ваш тест сгенерирован, перейти к тесту?', reply_markup=cfg.kb_yes_no)
            bot.register_next_step_handler(msg, test_main)
        elif message.text == 'Выход':
            msg = bot.send_message(message.chat.id, 'Понял, принял, сегодня без тестов')
            bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, желаемое количество вопросов в тесте превышает доступное количество по данной теме. Попробуйте ещё раз.{}'.format(e))
        msg = bot.send_message(message.chat.id, 'Из скольки вопросов должен состоять тест?\n(Можете написать своё количество вопросов)', reply_markup=cfg.kb_test_qty)
        bot.register_next_step_handler(msg, test_qty)


def test_main(message):
    try:
        if message.text == 'Да':
            while user_data[message.from_user.id][0] != 0:
                i = user_data_add[message.from_user.id]
                cursor.execute('SELECT answer FROM ' + str(datab_data[message.from_user.id]) + ' WHERE id != ' + str(test[message.from_user.id][i-1][0]) + '')
                rows = cursor.fetchall()
                kb_1234 = types.InlineKeyboardMarkup(row_width=2)
                kb_1 = types.InlineKeyboardButton(text="1️⃣", callback_data="1 " + str(i) + " " + str(message.from_user.id) + " test_answers")
                kb_2 = types.InlineKeyboardButton(text="2️⃣", callback_data="2 " + str(i) + " " + str(message.from_user.id) + " test_answers")
                kb_3 = types.InlineKeyboardButton(text="3️⃣", callback_data="3 " + str(i) + " " + str(message.from_user.id) + " test_answers")
                kb_4 = types.InlineKeyboardButton(text="4️⃣", callback_data="4 " + str(i) + " " + str(message.from_user.id) + " test_answers")
                kb_1234.add(kb_1, kb_2, kb_3, kb_4)
                if test[message.from_user.id][i-1][3] == 1:
                    oth = r.sample(rows, 3)
                    msg = bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + str(test[message.from_user.id][i-1][1]) + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(test[message.from_user.id][i-1][2]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 2:
                    oth = r.sample(rows, 3)
                    msg = bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[0][0]) + '\n'
                                                      '2) ' + str(test[message.from_user.id][i - 1][2]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 3:
                    oth = r.sample(rows, 3)
                    msg = bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[1][0]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(test[message.from_user.id][i - 1][2]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 4:
                    oth = r.sample(rows, 3)
                    msg = bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[2][0]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(test[message.from_user.id][i - 1][2]) + '\n', reply_markup=kb_1234)
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
            else:
                msg = bot.send_message(message.chat.id, 'Для проверки ответов воспользуйтесь кнопкой ниже', reply_markup=cfg.kb_test_end)
                user_data_test[message.from_user.id] = [0] * int(user_data[message.from_user.id][1])
                bot.register_next_step_handler(msg, callback)
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Ну, не хотите – как хотите')
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def test_mistakes(message):
    try:
        if message.text == 'Просмотреть ошибки':
            bot.send_message(message.chat.id, 'Правильные ответы ' + str(test_ringt_ans[message.from_user.id]) + '\nВаши ответы                ' + str(test_ans[message.from_user.id]) + '')
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        user_id = message.from_user.id

        sql = 'SELECT first_name FROM users WHERE user_id = {0}'.format(user_id)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if message.text.lower() == 'привет' and sup == None:
            bot.send_message(message.chat.id, 'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg (не обязательно)')
        elif message.text.lower() == 'привет' and sup != None:
            name = sup[0]
            bot.send_message(message.chat.id, 'Привет, {}'.format(name))
        if message.text.lower() == 'пока' and sup == None:
            bot.send_message(message.chat.id, 'Пока, Аноним')
        elif message.text.lower() == 'пока'and sup != None:
            name = sup[0]
            bot.send_message(message.chat.id, 'Пока, {}'.format(name))
    except Exception as e :
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel(message):
    try:
        if message.text == cfg.adm:
            msg = bot.send_message(message.chat.id, 'Добро пожаловать в админ панель', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
        else:
            msg = bot.send_message(message.chat.id, 'Неправильный пароль, попробуйте ещё раз')
            bot.register_next_step_handler(msg, admin_panel)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_what(message):
    try:
        mes = message.text
        if mes == 'Создать новую запись':
            msg = bot.send_message(message.chat.id, 'В какую таблицу добавлять запись?', reply_markup=cfg.kb_adm_table)
            bot.register_next_step_handler(msg, admin_panel_db_selection_create)
        elif mes == 'Удалить запись':
            msg = bot.send_message(message.chat.id, 'Из какой таблицы удалять запись', reply_markup=cfg.kb_adm_table)
            bot.register_next_step_handler(msg, admin_panel_db_selection_delete)
        elif mes == 'Просмотреть все записи':
            msg = bot.send_message(message.chat.id, 'Записи какой таблицы вы хотите просмотреть?', reply_markup=cfg.kb_adm_table)
            bot.register_next_step_handler(msg, admin_panel_db_view)
        elif mes == 'Выйти':
            msg = bot.send_message(message.chat.id, 'Вы вышли из админ панели')
            bot.register_next_step_handler(msg, send_text)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_db_view(message):
    try:
        bot.send_message(message.chat.id, 'Все записи из таблицы ' + message.text + '\n'
                                                'id\nВопрос\nОтвет\nОбразовтельные материалы')
        cursor.execute('SELECT * FROM ' + message.text + ' ORDER BY id')
        rows = cursor.fetchall()
        user_data[message.from_user.id] = [''] * 10
        i = 0
        for row in rows:
            if i < 10:
                user_data[message.from_user.id][i] = str(row[0]) + '\n------------------------------\n' + str(row[1]) + \
                '\n------------------------------\n' + str(row[2]) + '\n------------------------------\n' + str(row[3] + '\n\n\n\n')
                i += 1
            elif i == 10:
                i = 0
                user_data[message.from_user.id][i] = str(row[0]) + '\n------------------------------\n' + str(row[1]) + \
                '\n------------------------------\n' + str(row[2]) + '\n------------------------------\n' + str(row[3] + '\n\n\n\n')
                i += 1

                mes = user_data.get(message.from_user.id)
                msg = mes[0] + '\n' + mes[1] + '\n' + mes[2] + '\n' + mes[3] + '\n' + mes[4] + '\n' + mes[5] + '\n' + mes[6] + '\n' + mes[7] + '\n' + mes[8] + '\n' + mes[9]
                bot.send_message(message.chat.id, '{}'.format(msg))
        for row in user_data.get(message.from_user.id):
            if i > 0:
                i -= 1
                bot.send_message(message.chat.id, '{}'.format(row))
        msg = bot.send_message(message.chat.id, 'Что делаем дальше?', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_db_selection_create(message):
    try:
        s_db[message.from_user.id] = message.text
        msg = bot.send_message(message.chat.id, 'Введите вопрос')
        bot.register_next_step_handler(msg, admin_panel_create_question)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_db_selection_delete(message):
    try:
        s_db[message.from_user.id] = message.text
        msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
        bot.register_next_step_handler(msg, admin_panel_delete)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_question(message):
    try:
        que = [''] * 3
        que[0] = message.text
        datab_data[message.from_user.id] = que
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer(message):
    try:
        que = datab_data.get(message.from_user.id)
        que[1] = message.text
        datab_data[message.from_user.id] = que
        msg = bot.send_message(message.chat.id, 'Введите ссылку на дополнительный образовательный материал')
        bot.register_next_step_handler(msg, admin_panel_create_link)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_link(message):
    try:
        que = datab_data.get(message.from_user.id)
        que[2] = message.text
        sql = "INSERT INTO " + s_db.get(message.from_user.id) + " (question, answer, edu_mat) VALUES (%s, %s, %s)"
        val = (que[0], que[1], que[2])
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete(message):
    try:
        s_dr[message.from_user.id] = message.text
        sql = 'SELECT * FROM ' + s_db.get(message.from_user.id) + ' WHERE id = %s'
        val = (s_dr.get(message.from_user.id), )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        edu_mat_print = record[3]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}\nedu_mat: {}'.format(id_print, question_print, answer_print, edu_mat_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2(message):
    try:
        if message.text == 'Да':
            cursor.execute('DELETE FROM ' + s_db.get(message.from_user.id) + ' WHERE id = ' + s_dr.get(message.from_user.id) + '')
            db.commit()
            msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if "test_end" in call.data:
                cd = call.data.split()
                qty_right_answers = 0
                score = [0] * int(user_data[cd[1]][1])
                test_ans[cd[1]] = user_data_test.get(cd[1])
                right_answers = [0] * int(user_data[cd[1]][1])
                i = 0
                for row in test[cd[1]]:
                    right_answers[i] = row[3]
                    i += 1
                i = 0
                for row in test_ans[cd[1]]:
                    test_ans[cd[1]][i] = int(row)
                    i += 1
                i = 0
                for row in right_answers:
                    if row == test_ans[cd[1]][i]:
                        score[i] = 1
                        i += 1
                    elif row != test_ans[cd[1]][i]:
                        score[i] = 0
                        i += 1
                for row in score:
                    qty_right_answers += int(row)
                test_ringt_ans[cd[1]] = right_answers
                kb_test_mistakes = types.InlineKeyboardMarkup(row_width=1)
                kb_test_mistakes_check = types.InlineKeyboardButton(text="Просмотреть ошибки", callback_data="check " + str(cd[1]) + " test_mistakes")
                kb_test_mistakes.add(kb_test_mistakes_check)
                bot.send_message(call.message.chat.id, 'Ваш результат ' + str(qty_right_answers) + '/' +
                str(user_data[cd[1]][1]) + ' или ' + str(round(100 / int(user_data[cd[1]][1]) * int(qty_right_answers), 2)) + '%', reply_markup=kb_test_mistakes)
                msg = bot.send_message(call.message.chat.id, 'На ваш счёт зачисленно 0.000{}₿'.format(qty_right_answers))
                cursor.execute('SELECT btc FROM users WHERE user_id = ' + str(cd[1]) + '')
                old_btc = cursor.fetchone()[0]
                cursor.execute('UPDATE users SET btc = '  + str(old_btc + int(qty_right_answers)*0.0001) + ' WHERE user_id = ' + str(cd[1]) + '')
                db.commit()
                bot.register_next_step_handler(msg, callback)

            elif 'test_answers' in call.data:
                cd = call.data.split()
                answers = user_data_test.get(cd[2])
                answers[int(cd[1]) - 1] = int(cd[0])
                user_data_test[int(cd[2])] = answers

            elif 'grade' in call.data:
                cd = call.data.split()
                schedule = [cd[0], '', '']
                user_data[cd[1]] = schedule
                letters = cfg.letters[cd[0]]
                kb_letters = types.InlineKeyboardMarkup(row_width=3)
                kb_letter = []
                for letter in letters:
                    kb_letter.append(types.InlineKeyboardButton(text=letter, callback_data="" + letter + " " + str(cd[1]) + " letter"))
                if len(kb_letter) == 2: #Дикий котыль, надо исправить
                    kb_letters.add(kb_letter[0], kb_letter[1])
                elif len(kb_letter) == 3:
                    kb_letters.add(kb_letter[0], kb_letter[1], kb_letter[2])
                elif len(kb_letter) == 4:
                    kb_letters.add(kb_letter[0], kb_letter[1], kb_letter[2], kb_letter[3])
                elif len(kb_letter) == 5:
                    kb_letters.add(kb_letter[0], kb_letter[1], kb_letter[2], kb_letter[3], kb_letter[4])
                elif len(kb_letter) == 6:
                    kb_letters.add(kb_letter[0], kb_letter[1], kb_letter[2], kb_letter[3], kb_letter[4], kb_letter[5])
                elif len(kb_letter) == 7:
                    kb_letters.add(kb_letter[0], kb_letter[1], kb_letter[2], kb_letter[3], kb_letter[4], kb_letter[5], kb_letter[6])
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите букву', reply_markup=kb_letters)
                bot.register_next_step_handler(msg, callback)

            elif 'letter' in call.data:
                cd = call.data.split()
                schedule = user_data.get(cd[1])
                schedule[1] = cd[0]
                user_data[cd[1]] = schedule
                kb_weekday = types.InlineKeyboardMarkup(row_width=2)
                kb_weekday_mon = types.InlineKeyboardButton(text="Понедельник", callback_data="понедельник " + str(cd[1]) + " weekday")
                kb_weekday_tue = types.InlineKeyboardButton(text="Вторник", callback_data="вторник " + str(cd[1]) + " weekday")
                kb_weekday_wed = types.InlineKeyboardButton(text="Среда", callback_data="среда " + str(cd[1]) + " weekday")
                kb_weekday_thu = types.InlineKeyboardButton(text="Четверг", callback_data="четверг " + str(cd[1]) + " weekday")
                kb_weekday_fri = types.InlineKeyboardButton(text="Пятница", callback_data="пятница " + str(cd[1]) + " weekday")
                kb_weekday.add(kb_weekday_mon, kb_weekday_tue, kb_weekday_wed, kb_weekday_thu, kb_weekday_fri)
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите день недели', reply_markup=kb_weekday)
                bot.register_next_step_handler(msg, callback)

            elif 'weekday' in call.data:
                cd = call.data.split()
                schedule = user_data.get(cd[1])
                schedule[2] = cd[0]
                cursor.execute("SELECT lessons FROM schedule WHERE grade = {} AND letter = '{}' AND weekday = '{}'".format(schedule[0], schedule[1], schedule[2]))
                lessons = cursor.fetchone()
                mess = 'Расписание на ' + schedule[2] + ' у ' + schedule[0] + schedule[1] + ' класса\n', lessons[0]
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=mess[0] + mess[1])
                bot.register_next_step_handler(msg, start_help_message)

            elif 'ask_start' in call.data:
                cd = call.data.split()
                if cd[0] == 'viev':
                    kb_ask_t = types.InlineKeyboardMarkup(row_width=2)
                    kb_ask_t_math = types.InlineKeyboardButton(text="Математика", callback_data="math " + str(cd[1]) + " ask_viev")
                    kb_ask_t_phys = types.InlineKeyboardButton(text="Физика", callback_data="phys " + str(cd[1]) + " ask_viev")
                    kb_ask_t_inf = types.InlineKeyboardButton(text="Информатика", callback_data="inf " + str(cd[1]) + " ask_viev")
                    kb_ask_t.add(kb_ask_t_math, kb_ask_t_phys, kb_ask_t_inf)
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                                text='Вопросы какой категории вы бы хотели просмотреть?', reply_markup=kb_ask_t)
                    bot.register_next_step_handler(msg, callback)
                elif cd[0] == 'write':
                    kb_ask_t = types.InlineKeyboardMarkup(row_width=2)
                    kb_ask_t_math = types.InlineKeyboardButton(text="Математика", callback_data="math " + str(cd[1]) + " ask_write")
                    kb_ask_t_phys = types.InlineKeyboardButton(text="Физика", callback_data="phys " + str(cd[1]) + " ask_write")
                    kb_ask_t_inf = types.InlineKeyboardButton(text="Информатика", callback_data="inf " + str(cd[1]) + " ask_write")
                    kb_ask_t.add(kb_ask_t_math, kb_ask_t_phys, kb_ask_t_inf)
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                                text='Вопрос какой категории вы бы хотели задать?', reply_markup=kb_ask_t)
                    bot.register_next_step_handler(msg, callback)

            elif 'ask_write' in call.data:
                cd = call.data.split()
                user_data[cd[1]] = cd[0]
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Введите вопрос')
                bot.register_next_step_handler(msg, ask_set_question)

            elif 'ask_viev' in call.data:
                cd = call.data.split()
                cursor.execute("SELECT * FROM " + cd[0] + " ORDER BY id")
                rows = cursor.fetchall()
                user_data[cd[1]] = [''] * 10
                i = 0
                q = 1
                for row in rows:
                    if i < 10:
                        r2 = row[1]
                        l = len(r2)
                        r = r2[0:l // 2]
                        user_data[cd[1]][i] = r
                        i += 1
                    elif i == 10:
                        i = 0
                        r2 = row[1]
                        l = len(r2)
                        r = r2[0:l // 2]
                        user_data[cd[1]][i] = r
                        i += 1

                        mes = user_data.get(cd[1])
                        msg = str(q) + '. ' + mes[0] + '\n' + str(q + 1) + '. ' + mes[1] + '\n' + str(q + 2) + '. ' + mes[2] + '\n' + str(q + 3) + '. ' + mes[3] + '\n' + str(q + 4) + '. ' + mes[4] + '\n' + str(q + 5) + '. ' + mes[5] + '\n' + str(q + 6) + '. ' + mes[6] + '\n' + str(q + 7) + '. ' + mes[7] + '\n' + str(q + 8) + '. ' + mes[8] + '\n' + str(q + 9) + '. ' + mes[9]
                        bot.send_message(call.message.chat.id, '{}'.format(msg))
                        q += 10
                for row in user_data.get(cd[1]):
                    if i > 0:
                        i -= 1
                        bot.send_message(call.message.chat.id, str(q) + '. ' + '{}'.format(row))
                        q += 1
                kb_yes_no = types.InlineKeyboardMarkup(row_width=2)
                kb_yes = types.InlineKeyboardButton(text="Да", callback_data="yes " + cd[1] + " ask_except")
                kb_no = types.InlineKeyboardButton(text="Нет", callback_data="no " + cd[1] + " ask_except")
                kb_yes_no.add(kb_yes, kb_no)
                msg = bot.send_message(call.message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=kb_yes_no)
                bot.register_next_step_handler(msg, callback)

            elif 'ask_except' in call.data:
                cd = call.data.split()
                if cd[0] == 'yes':
                    kb_ask = types.InlineKeyboardMarkup(row_width=1)
                    kb_ask1 = types.InlineKeyboardButton(text="Просмотреть список доступных вопросов", callback_data="viev " + str(cd[1]) + " ask_start")
                    kb_ask2 = types.InlineKeyboardButton(text="Написать вручную", callback_data="write " + str(cd[1]) + " ask_start")
                    kb_ask.add(kb_ask1, kb_ask2)
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=
                    'Вы можете просмотреть список доступных вопросов (не рекомендуется) или задать вопрос вручную', reply_markup=kb_ask)
                    bot.register_next_step_handler(msg, callback)
                elif cd[0] == 'no':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы можете выбрать функцию или просмотрите список доступных /help')
                    bot.register_next_step_handler(msg, start_help_message)

            elif 'feedback' in call.data:
                cd = call.data.split()
                if cd[0] == 'complaint':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Опишите проблему')
                    bot.register_next_step_handler(msg, feedback_complaint)
                elif cd[0] == 'suggestion':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Напишите предложение')
                    bot.register_next_step_handler(msg, feedback_suggestion)

            elif 'cookie' in call.data:
                cd = call.data.split()
                if cd[0] == 'give':
                    cursor.execute('SELECT cookies FROM easter_egg WHERE id = 1')
                    cookies = cursor.fetchall()
                    count = cookies[0]
                    count_old = count = count[0]
                    count += 1
                    sql = ('UPDATE easter_egg SET cookies = %s WHERE cookies = %s')
                    val = (count, count_old)
                    cursor.execute(sql, val)
                    db.commit()
                    kb_cookie = types.InlineKeyboardMarkup(row_width=2)
                    kb_cookie_give = types.InlineKeyboardButton(text="Дать печеньку", callback_data="give " + str(cd[1]) + " cookie")
                    kb_cookie_exit = types.InlineKeyboardButton(text="Выйти", callback_data="exit " + str(cd[1]) + " cookie")
                    kb_cookie.add(kb_cookie_give, kb_cookie_exit)
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Всего печенек, {}'.format(count), reply_markup=kb_cookie)
                    bot.register_next_step_handler(msg, callback)
                elif cd[0] == 'exit':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы можете выбрать функцию или просмотрите список доступных /help')
                    bot.register_next_step_handler(msg, start_help_message)

            elif 'test_qty' in call.data:
                cd = call.data.split()
                user_data[cd[1]] = [cd[0], cd[0]]
                user_data_add[cd[1]] = 1
                kb_test = types.InlineKeyboardMarkup(row_width=2)
                kb_test_math = types.InlineKeyboardButton(text="Математика", callback_data="math " + str(cd[1]) + " test_table")
                kb_test_phys = types.InlineKeyboardButton(text="Физика", callback_data="phys " + str(cd[1]) + " test_table")
                kb_test_inf = types.InlineKeyboardButton(text="Информатика", callback_data="inf " + str(cd[1]) + " test_table")
                kb_test_exit = types.InlineKeyboardButton(text="Выход", callback_data="exit " + str(cd[1]) + " test_table")
                kb_test.add(kb_test_math, kb_test_phys, kb_test_inf, kb_test_exit)
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='По какой теме вы бы хотели проверить свои знания?', reply_markup=kb_test)
                bot.register_next_step_handler(msg, callback)

            elif 'test_table' in call.data:
                cd = call.data.split()
                datab_data[cd[1]] = cd[0]
                if cd[0] != 'exit':
                    cursor.execute('SELECT id, question, answer FROM ' + datab_data[cd[1]] + '')
                    rows = cursor.fetchall()
                    test[cd[1]] = random.sample(rows, int(user_data.get(cd[1])[0]))
                    ques = [[]] * int(user_data.get(cd[1])[0])
                    i = 0
                    for que in test[cd[1]]:
                        q = [0, '', '']
                        q[0] = que[0]
                        q[1] = que[1]
                        q[2] = que[2]
                        ques[i] = q
                        i += 1
                    i = 0
                    for que in ques:
                        q = [0, '', '', 0]
                        q[0] = que[0]
                        l = len(que[1])
                        q[1] = que[1][0:l // 2]
                        q[2] = que[2]
                        q[3] = random.randint(1, 4)
                        ques[i] = q
                        i += 1
                    test[cd[1]] = ques
                    kb_yes_no = types.InlineKeyboardMarkup(row_width=2)
                    kb_yes = types.InlineKeyboardButton(text="Да", callback_data="yes " + cd[1] + " test_main")
                    kb_no = types.InlineKeyboardButton(text="Нет", callback_data="no " + cd[1] + " test_main")
                    kb_yes_no.add(kb_yes, kb_no)
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ваш тест сгенерирован, перейти к тесту?', reply_markup=kb_yes_no)
                    bot.register_next_step_handler(msg, callback)
                elif cd[0] == 'Выход':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Понял, принял, сегодня без тестов')
                    bot.register_next_step_handler(msg, start_help_message)

            elif 'test_main' in call.data:
                cd = call.data.split()
                if cd[0] == 'yes':
                    while user_data[cd[1]][0] != 0:
                        i = user_data_add[cd[1]]
                        cursor.execute('SELECT answer FROM ' + str(datab_data[cd[1]]) + ' WHERE id != ' + str(test[cd[1]][i - 1][0]) + '')
                        rows = cursor.fetchall()
                        kb_1234 = types.InlineKeyboardMarkup(row_width=2)
                        kb_1 = types.InlineKeyboardButton(text="1️⃣", callback_data="1 " + str(i) + " " + str(cd[1]) + " test_answers")
                        kb_2 = types.InlineKeyboardButton(text="2️⃣", callback_data="2 " + str(i) + " " + str(cd[1]) + " test_answers")
                        kb_3 = types.InlineKeyboardButton(text="3️⃣", callback_data="3 " + str(i) + " " + str(cd[1]) + " test_answers")
                        kb_4 = types.InlineKeyboardButton(text="4️⃣", callback_data="4 " + str(i) + " " + str(cd[1]) + " test_answers")
                        kb_1234.add(kb_1, kb_2, kb_3, kb_4)
                        if test[cd[1]][i - 1][3] == 1:
                            oth = random.sample(rows, 3)
                            msg = bot.send_message(call.message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                                        '' + str(test[cd[1]][i - 1][1]) + '\n\n'
                                                                        'Варианты ответов:\n'
                                                                        '1) ' + str(test[cd[1]][i - 1][2]) + '\n'
                                                                        '2) ' + str(oth[0][0]) + '\n'
                                                                        '3) ' + str(oth[1][0]) + '\n'
                                                                        '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                            user_data[cd[1]][0] = int(user_data[cd[1]][0]) - 1
                            user_data_add[cd[1]] = int(user_data_add[cd[1]]) + 1
                        elif test[cd[1]][i - 1][3] == 2:
                            oth = random.sample(rows, 3)
                            msg = bot.send_message(call.message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                                        '' + test[cd[1]][i - 1][1] + '\n\n'
                                                                        'Варианты ответов:\n'
                                                                        '1) ' + str(oth[0][0]) + '\n'
                                                                        '2) ' + str(test[cd[1]][i - 1][2]) + '\n'
                                                                        '3) ' + str(oth[1][0]) + '\n'
                                                                        '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                            user_data[cd[1]][0] = int(user_data[cd[1]][0]) - 1
                            user_data_add[cd[1]] = int(user_data_add[cd[1]]) + 1
                        elif test[cd[1]][i - 1][3] == 3:
                            oth = random.sample(rows, 3)
                            msg = bot.send_message(call.message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                                        '' + test[cd[1]][i - 1][1] + '\n\n'
                                                                        'Варианты ответов:\n'
                                                                        '1) ' + str(oth[1][0]) + '\n'
                                                                        '2) ' + str(oth[0][0]) + '\n'
                                                                        '3) ' + str(test[cd[1]][i - 1][2]) + '\n'
                                                                        '4) ' + str(oth[2][0]) + '\n', reply_markup=kb_1234)
                            user_data[cd[1]][0] = int(user_data[cd[1]][0]) - 1
                            user_data_add[cd[1]] = int(user_data_add[cd[1]]) + 1
                        elif test[cd[1]][i - 1][3] == 4:
                            oth = random.sample(rows, 3)
                            msg = bot.send_message(call.message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                                        '' + test[cd[1]][i - 1][1] + '\n\n'
                                                                        'Варианты ответов:\n'
                                                                        '1) ' + str(oth[2][0]) + '\n'
                                                                        '2) ' + str(oth[0][0]) + '\n'
                                                                        '3) ' + str(oth[1][0]) + '\n'
                                                                        '4) ' + str(test[cd[1]][i - 1][2]) + '\n', reply_markup=kb_1234)
                            user_data[cd[1]][0] = int(user_data[cd[1]][0]) - 1
                            user_data_add[cd[1]] = int(user_data_add[cd[1]]) + 1
                    else:
                        kb_test_end = types.InlineKeyboardMarkup(row_width=2)
                        kb_test_end_end = types.InlineKeyboardButton(text="Закончить прохождение теста", callback_data="end " + str(cd[1]) + " test_end")
                        kb_test_end.add(kb_test_end_end)
                        msg = bot.send_message(call.message.chat.id, 'Для проверки ответов воспользуйтесь кнопкой ниже', reply_markup=kb_test_end)
                        user_data_test[cd[1]] = [0] * int(user_data[cd[1]][1])
                        bot.register_next_step_handler(msg, callback)
                elif cd[0] == 'no':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ну, не хотите – как хотите')

            elif 'test_mistakes' in call.data:
                cd = call.data.split()
                if cd[0] == 'check':
                    msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Правильные ответы ' + str(test_ringt_ans[cd[1]]) + '\nВаши ответы                ' + str(test_ans[cd[1]]) + '')
                    bot.register_next_step_handler(msg, start_help_message)

    except Exception as e:
        print(repr(e))

bot.polling()
