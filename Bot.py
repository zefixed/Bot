import telebot
import mysql.connector
import config as cfg

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
name = ''
question = ''


class Datab:
    def __init__(self, question):
        self.question = question
        self.answer = ''


class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''


@bot.message_handler(commands=['start', 'ask', 'help', 'reg', 'rereg', 'info', 'adm', 'feedback', 'cookie'])
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
                                              '7. /feedback (Позволяет сообщить об ошибке или предложить нововведение)')
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
        elif message.text == '/adm':
            adm = bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(adm, admin_panel)
        elif message.text == '/feedback':
            msg = bot.send_message(message.chat.id, 'О чём вы бы хотели сообщить?', reply_markup=cfg.kb_fb)
            bot.register_next_step_handler(msg, feedback_start)
        elif message.text == '/cookie':
            msg = bot.send_message(message.chat.id, 'Покормить разработчиков', reply_markup=cfg.kb_cookie)
            bot.register_next_step_handler(msg, easter_egg)
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
        if message.text == 'Корни, степени, логарифмы':
            cursor.execute('SELECT * FROM radical_power_logarithm ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r2 = row[1]
                bot.send_message(message.chat.id,'{}'.format(r2))
            msg = bot.send_message(message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=cfg.kb_yes_no)
            bot.register_next_step_handler(msg, ask_except)
        elif message.text == 'Тригонометрия':
            cursor.execute('SELECT * FROM trigonometry ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r2 = row[1]
                bot.send_message(message.chat.id, '{}'.format(r2))
            msg = bot.send_message(message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=cfg.kb_yes_no)
            bot.register_next_step_handler(msg, ask_except)
        elif message.text == 'Теория вероятностей':
            cursor.execute('SELECT * FROM probability_theory ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r2 = row[1]
                bot.send_message(message.chat.id, '{}'.format(r2))
            msg = bot.send_message(message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=cfg.kb_yes_no)
            bot.register_next_step_handler(msg, ask_except)
        elif message.text == 'Геометрические понятия':
            cursor.execute('SELECT * FROM geometric_concepts ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r2 = row[1]
                bot.send_message(message.chat.id, '{}'.format(r2))
            msg = bot.send_message(message.chat.id, 'Хотите задать вопрос или просмотреть доступные вопросы ещё раз?', reply_markup=cfg.kb_yes_no)
            bot.register_next_step_handler(msg, ask_except)
        elif message.text == 'Алгебраические понятия и интересные вопросы':
            cursor.execute('SELECT * FROM algebraic_concepts ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r2 = row[1]
                bot.send_message(message.chat.id, '{}'.format(r2))
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
        sql = "SELECT answer, edu_mat FROM radical_power_logarithm WHERE question LIKE '%"+question+"%'"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for rows in all_rows:
            answer = rows[0]
            edu_mat = rows[1]
        print(all_rows)
        bot.send_message(message.chat.id, '{}'.format(answer))
        bot.send_message(message.chat.id, 'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                                          '{}'.format(edu_mat))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                               'Ошибка, ответ на ваш вопрос не найден. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_trigonometry(message):
    try:
        question = message.text
        sql = "SELECT answer FROM trigonometry WHERE question LIKE '%" + question + "%'"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for rows in all_rows:
            answer = rows[0]
            edu_mat = rows[1]
        print(all_rows)
        bot.send_message(message.chat.id, '{}'.format(answer))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(edu_mat))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         'Ошибка, ответ на ваш вопрос не найден. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_probability_theory(message):
    try:
        question = message.text
        sql = "SELECT answer FROM probability_theory WHERE question LIKE '%" + question + "%'"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for rows in all_rows:
            answer = rows[0]
            edu_mat = rows[1]
        print(all_rows)
        bot.send_message(message.chat.id, '{}'.format(answer))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(edu_mat))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         'Ошибка, ответ на ваш вопрос не найден. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_geometric_concepts(message):
    try:
        question = message.text
        sql = "SELECT answer FROM geometric_concepts WHERE question LIKE '%" + question + "%'"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for rows in all_rows:
            answer = rows[0]
            edu_mat = rows[1]
        print(all_rows)
        bot.send_message(message.chat.id, '{}'.format(answer))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(edu_mat))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         'Ошибка, ответ на ваш вопрос не найден. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)


def ask_set_question_algebraic_concepts(message):
    try:
        question = message.text
        sql = "SELECT answer FROM algebraic_concepts WHERE question LIKE '%" + question + "%'"
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for rows in all_rows:
            answer = rows[0]
            edu_mat = rows[1]
        print(all_rows)
        bot.send_message(message.chat.id, '{}'.format(answer))
        bot.send_message(message.chat.id,
                         'Дополнительные образовательные материалы по данному вопросу вы можете найти по ссылке '
                         '{}'.format(edu_mat))
        msg = bot.send_message(message.chat.id, 'Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, ask_except)
    except Exception:
        msg = bot.send_message(message.chat.id,
                         'Ошибка, ответ на ваш вопрос не найден. Попробуйте переформулировать вопрос или задать другой. Хотите задать вопрос ещё раз?', reply_markup=cfg.kb_yes_no)
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


def feedback_start(message):
    try:
        if message.text == 'Проблема':
            msg = bot.send_message(message.chat.id, 'Опишите проблему')
            bot.register_next_step_handler(msg, feedback_problem)
        elif message.text == 'Пожелание':
            msg = bot.send_message(message.chat.id, 'Напишите пожелание')
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


def reg_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)

        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, reg_lastname_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def reg_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text

        sql = "INSERT INTO users (first_name, last_name, user_id) \
                                  VALUES (%s, %s, %s)"
        val = (user.first_name, user.last_name, user_id)
        cursor.execute(sql, val)
        db.commit()

        msg = bot.send_message(message.chat.id, "Вы успешно зарегистрированны!")
        bot.register_next_step_handler(msg, start_help_message)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def rereg_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)

        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, rereg_lastname_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def rereg_lastname_step(message):
    user_id = message.from_user.id
    user = user_data[user_id]
    user.last_name = message.text

    sql = 'UPDATE users SET first_name = %s, last_name = %s WHERE user_id = {0}'.format(user_id)
    val = (user.first_name, user.last_name)
    cursor.execute(sql, val)
    db.commit()

    bot.send_message(message.chat.id, "Вы успешно перерегистрированны!")


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        user_id = message.from_user.id

        sql = 'SELECT first_name FROM users WHERE user_id = {0}'.format(user_id)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if message.text.lower() == 'привет'and sup == None:
            bot.send_message(message.chat.id,'Привет, если хочешь чтобы я к тебе обращался по имени введи /reg (не обязательно)')
        elif message.text.lower() == 'привет'and sup != None:
            name = sup[0]
            bot.send_message(message.chat.id, 'Привет, {}'.format(name))
        if message.text.lower() == 'пока' and sup == None:
            bot.send_message(message.chat.id,'Пока, Аноним')
        elif message.text.lower() == 'пока'and sup != None:
            name = sup[0]
            bot.send_message(message.chat.id, 'Пока, {}'.format(name))
    except Exception as e :
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


@bot.message_handler(content_types=['text'])
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
        if mes == 'Создать новую запись в БД':
            msg = bot.send_message(message.chat.id, 'В какую БД добавлять запись?', reply_markup=cfg.kb_admbd)
            bot.register_next_step_handler(msg, admin_panel_db_selection_create)
        elif mes == 'Удалить запись из БД':
            msg = bot.send_message(message.chat.id, 'Из какой БД удалять запись', reply_markup=cfg.kb_admbd)
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
        if message.text == 'radical_power_logarithm':
            msg = bot.send_message(message.chat.id, 'Все записи из таблицы radical_power_logarithm\n'
                                              'id\nВопрос\nОтвет', reply_markup=cfg.kb_admc)
            cursor.execute('SELECT * FROM radical_power_logarithm ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                bot.send_message(message.chat.id, '{}\n------------------------------\n{}\n------------------------------\n{}'.format(r1, r2, r3))
            bot.register_next_step_handler(msg, admin_panel_what)
        elif message.text == 'trigonometry':
            msg = bot.send_message(message.chat.id, 'Все записи из таблицы trigonometry\n'
                                                    'id         Вопрос        Ответ', reply_markup=cfg.kb_admc)
            cursor.execute('SELECT * FROM trigonometry ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                bot.send_message(message.chat.id, '{}\n------------------------------\n{}\n------------------------------\n{}'.format(r1, r2, r3))
            bot.register_next_step_handler(msg, admin_panel_what)
        elif message.text == 'probability_theory':
            msg = bot.send_message(message.chat.id, 'Все записи из таблицы probability_theory\n'
                                                    'id         Вопрос        Ответ', reply_markup=cfg.kb_admc)
            cursor.execute('SELECT * FROM probability_theory ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                bot.send_message(message.chat.id, '{}\n------------------------------\n{}\n------------------------------\n{}'.format(r1, r2, r3))
            bot.register_next_step_handler(msg, admin_panel_what)
        elif message.text == 'geometric_concepts':
            msg = bot.send_message(message.chat.id, 'Все записи из таблицы geometric_concepts\n'
                                                    'id         Вопрос        Ответ', reply_markup=cfg.kb_admc)
            cursor.execute('SELECT * FROM geometric_concepts ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                bot.send_message(message.chat.id, '{}\n------------------------------\n{}\n------------------------------\n{}'.format(r1, r2, r3))
            bot.register_next_step_handler(msg, admin_panel_what)
        elif message.text == 'algebraic_concepts':
            msg = bot.send_message(message.chat.id, 'Все записи из таблицы algebraic_concepts\n'
                                                    'id         Вопрос        Ответ', reply_markup=cfg.kb_admc)
            cursor.execute('SELECT * FROM algebraic_concepts ORDER BY id')
            rows = cursor.fetchall()
            for row in rows:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                bot.send_message(message.chat.id, '{}\n------------------------------\n{}\n------------------------------\n{}'.format(r1, r2, r3))
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_db_selection_create(message):
    try:
        if message.text =='radical_power_logarithm':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question_radicalpowerlogarithm)
        elif message.text =='trigonometry':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question_trigonometry)
        elif message.text =='probability_theory':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question_probability_theory)
        elif message.text =='geometric_concepts':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question_geometric_concepts)
        elif message.text =='algebraic_concepts':
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question_algebraic_concepts)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_db_selection_delete(message):
    try:
        if message.text =='radical_power_logarithm':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete_radicalpowerlogarithm)
        elif message.text =='trigonometry':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete_trigonometry)
        elif message.text =='probability_theory':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete_probability_theory)
        elif message.text =='geometric_concepts':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete_geometric_concepts)
        elif message.text =='algebraic_concepts':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete_algebraic_concepts)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


######################CREATE######################
def admin_panel_create_question_radicalpowerlogarithm(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer_radicalpowerlogarithm)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer_radicalpowerlogarithm(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO radical_power_logarithm (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_question_trigonometry(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer_trigonometry)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer_trigonometry(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO trigonometry (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_question_probability_theory(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer_probability_theory)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer_probability_theory(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO probability_theory (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_question_geometric_concepts(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer_geometric_concepts)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer_geometric_concepts(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO geometric_concepts (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_question_algebraic_concepts(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)

        Datab.question = message.text
        msg = bot.send_message(message.chat.id, 'Введите ответ')
        bot.register_next_step_handler(msg, admin_panel_create_answer_algebraic_concepts)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_create_answer_algebraic_concepts(message):
    try:
        datab_id = message.from_user.id
        datab_data[datab_id] = Datab(message.text)



        datab_id = message.from_user.id
        datab = datab_data[datab_id]
        datab.answer = message.text

        sql = "INSERT INTO algebraic_concepts (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

######################DELETE######################
def admin_panel_delete_radicalpowerlogarithm(message):
    try:
        id = message.text
        sql = 'SELECT * FROM radical_power_logarithm WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2_radicalpowerlogarithm)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2_radicalpowerlogarithm(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3_radicalpowerlogarithm)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3_radicalpowerlogarithm(message):
    try:
        id = message.text
        sql = 'DELETE FROM radical_powerlogarithm WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete_trigonometry(message):
    try:
        id = message.text
        sql = 'SELECT * FROM trigonometry WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2_trigonometry)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2_trigonometry(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3_trigonometry)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3_trigonometry(message):
    try:
        id = message.text
        sql = 'DELETE FROM trigonometry WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete_probability_theory(message):
    try:
        id = message.text
        sql = 'SELECT * FROM probability_theory WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2_probability_theory)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2_probability_theory(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3_probability_theory)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3_probability_theory(message):
    try:
        id = message.text
        sql = 'DELETE FROM probability_theory WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete_geometric_concepts(message):
    try:
        id = message.text
        sql = 'SELECT * FROM geometric_concepts WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2_geometric_concepts)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2_geometric_concepts(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3_geometric_concepts)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3_geometric_concepts(message):
    try:
        id = message.text
        sql = 'DELETE FROM geometric_concepts WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete_algebraic_concepts(message):
    try:
        id = message.text
        sql = 'SELECT * FROM algebraic_concepts WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        record = cursor.fetchone()
        id_print = record[0]
        question_print = record[1]
        answer_print = record[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2_algebraic_concepts)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)


def admin_panel_delete2_algebraic_concepts(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напишите ещё раз id удаляемой записи)')
            bot.register_next_step_handler(msg, admin_panel_delete3_algebraic_concepts)
        elif message.text == 'Нет':
            msg = bot.send_message(message.chat.id, 'Попробуйте заново', reply_markup=cfg.kb_admc)
            bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def admin_panel_delete3_algebraic_concepts(message):
    try:
        id = message.text
        sql = 'DELETE FROM algebraic_concepts WHERE id = %s'
        val = (id,)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))



bot.polling()
