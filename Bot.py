import telebot
import mysql.connector
import config as cfg
import random as r

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Testdb"
)

cursor = db.cursor()


bot = telebot.TeleBot(cfg.token)

datab_data = {}
user_data = {}
user_data_add = {}  # additional user data
s_db = {}           # select table
s_dr = {}           # delete record
test = {}           # [id, question, answer, position]
test_ans = {}       # answers from user
test_ringt_ans = {}
name = ''
question = ''


@bot.message_handler(commands=['start', 'ask', 'help', 'reg', 'rereg', 'info', 'feedback', 'cookie', 'acc_info', 'test', 'adm'])
def start_help_message(message):
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=cfg.kb)
        elif message.text == '/ask':
            msg = bot.send_message(message.chat.id, 'Вы можете просмотреть список доступных вопросов (не рекомендуется) или задать вопрос вручную', reply_markup=cfg.kb_ask)
            bot.register_next_step_handler(msg, ask_start)
        elif message.text == '/help':
            bot.send_message(message.chat.id, 'Доступные команды\n'
                                              '1. /start (Используется для начала общения со мной)\n'
                                              '2. /ask (Позволяет задать мне вопрос)\n'
                                              '3. /help (Показывает известные мне команды)\n'
                                              '4. /reg (Позволяет мне обращаться к тебе по имени)\n'
                                              '5. /rereg (Позволяет перерегистрироваться)\n'
                                              '6. /info (Показывает информацию обо мне)\n'
                                              '7. /feedback (Позволяет сообщить об ошибке или предложить нововведение)\n'
                                              '8. /acc_info (Позволяет просмотреть инфромацию об аккаунте в боте)\n'
                                              '9. /test (Позволяет проверить свои знания)')
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
            msg = bot.send_message(message.chat.id, 'О чём вы бы хотели сообщить?', reply_markup=cfg.kb_fb)
            bot.register_next_step_handler(msg, feedback_start)
        elif message.text == '/cookie':
            msg = bot.send_message(message.chat.id, 'Покормить разработчиков', reply_markup=cfg.kb_cookie)
            bot.register_next_step_handler(msg, easter_egg)
        elif message.text == '/acc_info':
            bot.send_message(message.chat.id, 'Информация об аккаунте')
            cursor.execute("SELECT * FROM users WHERE user_id = " + str(message.from_user.id) + "")
            i = cursor.fetchall()
            i = i[0]
            bot.send_message(message.chat.id, 'Имя: {}\n'
                                              'Фамилия: {}\n'
                                              'id в боте: {}\n'
                                              'Telegram id: {}\n'
                                              'Дата и время первичной регистрации в боте: {}\n'
                                              'Дата и время последней перерегистрации в боте: {}'.format(i[2], i[3], i[0], i[1], i[4], i[5]))
        elif message.text == '/test':
            msg = bot.send_message(message.chat.id, 'Из скольки вопросов должен состоять тест?\n(Можете написать своё количество вопросов)', reply_markup=cfg.kb_test_qty)
            bot.register_next_step_handler(msg, test_qty)
        elif message.text == '/adm':
            msg = bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(msg, admin_panel)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка, информация об аккаунте недоступна. Возможная причина ошибки - аккаунт не создан')


def ask_start(message):
    try:
        if message.text == 'Просмотреть список доступных вопросов':
            msg = bot.send_message(message.chat.id, 'Вопросы какой категории вы бы хотели просмотреть?', reply_markup=cfg.kb_ask_t)
            bot.register_next_step_handler(msg, ask_viev)
        elif message.text == 'Написать вручную':
            msg = bot.send_message(message.chat.id, 'Вопрос какой категории вы бы хотели задать?', reply_markup=cfg.kb_ask_t)
            bot.register_next_step_handler(msg, ask_set_table)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def ask_viev(message):
    try:
        table = message.text
        if message.text == 'Корни, степени, логарифмы':
            table = 'radical_power_logarithm'
        elif message.text == 'Тригонометрия':
            table = 'trigonometry'
        elif message.text == 'Теория вероятностей':
            table = 'probability_theory'
        elif message.text == 'Геометрические понятия':
            table = 'geometric_concepts'
        elif message.text == 'Алгебраические понятия и интересные вопросы':
            table = 'algebraic_concepts'
        cursor.execute("SELECT * FROM " + table + " ORDER BY id")
        rows = cursor.fetchall()
        for row in rows:
            r2 = row[1]
            l = len(r2)
            r = r2[0:l//2]
            bot.send_message(message.chat.id,'{}'.format(r))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def ask_set_table(message):
    try:
        if message.text == 'Корни, степени, логарифмы':
            msg = bot.send_message(message.chat.id,'Введите вопрос')
            bot.register_next_step_handler(msg, ask_set_question_radical_power_logarithm)
        elif message.text == 'Тригонометрия':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, ask_set_question_trigonometry)
        elif message.text == 'Теория вероятностей':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, ask_set_question_probability_theory)
        elif message.text == 'Геометрические понятия':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, ask_set_question_geometric_concepts)
        elif message.text == 'Алгебраические понятия и интересные вопросы':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, ask_set_question_algebraic_concepts)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def ask_set_question_radical_power_logarithm(message):
    try:
        question = message.text
        sql = "SELECT answer, edu_mat FROM radical_power_logarithm WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                               """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_trigonometry(message):
    try:
        question = message.text
        sql = "SELECT answer, edu_mat FROM trigonometry WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                               """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_probability_theory(message):
    try:
        question = message.text
        sql = "SELECT answer, edu_mat FROM probability_theory WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_geometric_concepts(message):
    try:
        question = message.text
        sql = "SELECT answer, edu_mat FROM geometric_concepts WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_algebraic_concepts(message):
    try:
        question = message.text
        sql = "SELECT answer, edu_mat FROM algebraic_concepts WHERE MATCH (question) AGAINST ('" + question + "')"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        row = all_rows[0]
        bot.send_message(message.chat.id, '{}'.format(row[0]))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(row[1]))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         """Ошибка, ответ на ваш вопрос не найден. Проверьте правильность ввода вопроса. Вопрос не должен содержать кавычек <"> <'> и запятых <,>. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?""", reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_except(message):
    try:
        mes = message.text
        if mes == 'Да':
            msg = bot.send_message(message.chat.id,
                                   'Вы можете просмотреть список доступных вопросов (не рекомендуется) или задать вопрос вручную', reply_markup=cfg.kb_ask)
            bot.register_next_step_handler(msg, ask_start)
        elif mes == 'Нет':
            msg = bot.send_message(message.chat.id, 'Вы можете выбрать функцию или просмотрите список доступных /help')
            bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


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


def feedback_start(message):
    try:
        if message.text == 'Проблема':
            msg = bot.send_message(message.chat.id, 'Опишите проблему')
            bot.register_next_step_handler(msg, feedback_problem)
        elif message.text == 'Предложение':
            msg = bot.send_message(message.chat.id, 'Напишите предложение')
            bot.register_next_step_handler(msg, feedback_request)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def feedback_problem(message):
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


def feedback_request(message):
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


def easter_egg(message):
    try:
        if message.text == 'Дать печеньку':
            cursor.execute('SELECT cookies FROM easter_egg WHERE id = 1')
            cookies = cursor.fetchall()
            count = cookies[0]
            count_old = count = count[0]
            count +=1
            sql = ('UPDATE easter_egg SET cookies = %s WHERE cookies = %s')
            val = (count, count_old)
            cursor.execute(sql, val)
            db.commit()
            msg = bot.send_message(message.chat.id, 'Всего печенек, {}'.format(count), reply_markup=cfg.kb_cookie)
            bot.register_next_step_handler(msg, easter_egg)
        elif message.text == 'Выйти':
            msg = bot.send_message(message.chat.id, 'Вы можете выбрать функцию или просмотрите список доступных /help')
            bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def acc_info(message):
    try:
        cursor.execute("SELECT * FROM users WHERE user_id = " + message.from_user.id + "")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

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
        if message.text == 'Корни, степени, логарифмы':
            datab_data[message.from_user.id] = 'radical_power_logarithm'
        elif message.text == 'Тригонометрия':
            datab_data[message.from_user.id] = 'trigonometry'
        elif message.text == 'Теория вероятностей':
            datab_data[message.from_user.id] = 'probability_theory'
        elif message.text == 'Геометрические понятия':
            datab_data[message.from_user.id] = 'geometric_concepts'
        elif message.text == 'Алгебраические понятия и интересные вопросы':
            datab_data[message.from_user.id] = 'algebraic_concepts'
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
                if test[message.from_user.id][i-1][3] == 1:
                    oth = r.sample(rows, 3)
                    bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + str(test[message.from_user.id][i-1][1]) + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(test[message.from_user.id][i-1][2]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n')
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 2:
                    oth = r.sample(rows, 3)
                    bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[0][0]) + '\n'
                                                      '2) ' + str(test[message.from_user.id][i - 1][2]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n')
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 3:
                    oth = r.sample(rows, 3)
                    bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[1][0]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(test[message.from_user.id][i - 1][2]) + '\n'
                                                      '4) ' + str(oth[2][0]) + '\n')
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
                elif test[message.from_user.id][i-1][3] == 4:
                    oth = r.sample(rows, 3)
                    bot.send_message(message.chat.id, 'Вопрос №' + str(i) + '\n'
                                                      '' + test[message.from_user.id][i - 1][1] + '\n\n'
                                                      'Варианты ответов:\n'
                                                      '1) ' + str(oth[2][0]) + '\n'
                                                      '2) ' + str(oth[0][0]) + '\n'
                                                      '3) ' + str(oth[1][0]) + '\n'
                                                      '4) ' + str(test[message.from_user.id][i - 1][2]) + '\n')
                    user_data[message.from_user.id][0] = int(user_data[message.from_user.id][0]) - 1
                    user_data_add[message.from_user.id] = int(user_data_add[message.from_user.id]) + 1
            else:
                msg = bot.send_message(message.chat.id, 'В ответе напишите последовательность цифр верных ответов на вопросы по порядку их следования в тесте через пробел. Если затрудняетесь ответить на вопрос напишите 0')
                bot.register_next_step_handler(msg, test_answers)
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Ну, не хотите – как хотите')
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def test_answers(message):
    try:
        qty_right_answers = 0
        score = [0] * int(user_data[message.from_user.id][1])
        test_ans[message.from_user.id] = message.text.split()
        bot.send_message(message.chat.id, 'Ваш ответ принят')
        right_answers = [0] * int(user_data[message.from_user.id][1])
        i = 0
        for row in test[message.from_user.id]:
            right_answers[i] = row[3]
            i += 1
        i = 0
        for row in test_ans[message.from_user.id]:
            test_ans[message.from_user.id][i] = int(row)
            i += 1
        i = 0
        for row in right_answers:
            if row == test_ans[message.from_user.id][i]:
                score[i] = 1
                i += 1
            elif row != test_ans[message.from_user.id][i]:
                score[i] = 0
                i += 1
        for row in score:
            qty_right_answers += int(row)
        test_ringt_ans[message.from_user.id] = right_answers
        msg = bot.send_message(message.chat.id, 'Ваш результат ' + str(qty_right_answers) + '/' + str(user_data[message.from_user.id][1]) + '\
 или ' + str(round(100 / int(user_data[message.from_user.id][1]) * int(qty_right_answers), 2)) + '%', reply_markup=cfg.kb_test_mistakes)
        bot.register_next_step_handler(msg, test_mistakes)
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
                bot.send_message(message.chat.id, 'Неправильный пароль, попробуйте ещё раз', reply_markup=cfg.kb_adm)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_what(message):
    try:
        mes = message.text
        if mes == 'Создать новую запись':
            msg = bot.send_message(message.chat.id, 'В какую таблицу добавлять запись?', reply_markup=cfg.kb_admbd)
            bot.register_next_step_handler(msg, admin_panel_db_selection_create)
        elif mes == 'Удалить запись':
            msg = bot.send_message(message.chat.id, 'Из какой таблицы удалять запись', reply_markup=cfg.kb_admbd)
            bot.register_next_step_handler(msg, admin_panel_db_selection_delete)
        elif mes == 'Просмотреть все записи':
            msg = bot.send_message(message.chat.id, 'Записи какой таблицы вы хотите просмотреть?', reply_markup=cfg.kb_admbd)
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
        for row in rows:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            r4 = row[3]
            bot.send_message(message.chat.id,
                             '{}\n------------------------------\n{}\n------------------------------\n{}\n------------------------------\n{}'.format(
                                 r1, r2, r3, r4))
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
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
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

bot.polling()
