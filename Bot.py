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

class Datab:
    def __init__(self, question):
        self.question = question
        self.answer = ''

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''

@bot.message_handler(commands=['start', 'help', 'reg','adm', 'rereg'])
def start_help_message(message):
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=cfg.kb)
        elif message.text == '/help':
            bot.send_message(message.chat.id, 'Доступные команду\n'
                                              '1. /start (Используется для начала общения со мной)\n'
                                              '2. /help (Показывает известные мне команды)\n'
                                              '3. /reg (Позволяет мне обращаться к тебе по имени)\n'
                                              '4. /rereg (Позволяет перерегистрироваться)\n')
        elif message.text == '/reg':
            name = bot.send_message(message.chat.id, 'Введите имя')
            bot.register_next_step_handler(name, reg_firstname_step)
        elif message.text == '/adm':
            adm = bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(adm, admin_panel)
        elif message.text == '/rereg':
            name = bot.send_message(message.chat.id, 'Введите имя')
            bot.register_next_step_handler(name, rereg_firstname_step)
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

        bot.send_message(message.chat.id, "Вы успешно зарегистрированны!")
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
            msg = bot.send_message(message.chat.id, 'Введите вопрос')
            bot.register_next_step_handler(msg, admin_panel_create_question)
        elif mes == 'Удалить запись из БД':
            msg = bot.send_message(message.chat.id, 'Введите id записи которую хотите удалить')
            bot.register_next_step_handler(msg, admin_panel_delete)
        elif mes == 'Выйти':
            msg = bot.send_message(message.chat.id, 'Вы вышли из админ панели')
            bot.register_next_step_handler(msg, send_text)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

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

        sql = "INSERT INTO articles (question, answer) \
                                          VALUES (%s, %s)"
        val = (Datab.question, datab.answer)
        cursor.execute(sql, val)
        db.commit()
        msg = bot.send_message(message.chat.id, 'Запись добавленна', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

def admin_panel_delete(message):
    try:
        id = message.text
        sql = 'SELECT * FROM articles WHERE id = %s'
        val = (id, )
        cursor.execute(sql, val)
        entry = cursor.fetchone()
        id_print = entry[0]
        question_print = entry[1]
        answer_print = entry[2]
        bot.send_message(message.chat.id, 'id: {}\nquestion: {}\nanswer: {}'.format(id_print, question_print, answer_print))
        msg = bot.send_message(message.chat.id, 'Вы уверены что хотите удалить эту запись?', reply_markup=cfg.kb_yes_no)
        bot.register_next_step_handler(msg, admin_panel_delete2)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Запись не найдена, попробуйте ещё раз', reply_markup=cfg.kb_admc)
        bot.register_next_step_handler(msg, admin_panel_what)

def admin_panel_delete2(message):
    try:
        if message.text == 'Да':
            msg = bot.send_message(message.chat.id, 'Подтвердите удаление (Напииште ещё раз id удаляемой записи)')
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

bot.polling()

