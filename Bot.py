import telebot
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Testdb"
)

cursor = db.cursor()

bot = telebot.TeleBot('1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY')

kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

user_data = {}
name = ''

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''

@bot.message_handler(commands=['start', 'help', 'reg','adm', 'rereg'])
def start_help_message(message):
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Привет, если не знаешь как мной пользоваться или ты тут в первый раз можешь написать /help для просмотра доступных команд', reply_markup=kb)
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
            adm = bot.send_message(message.chat.id,'Введите пароль')
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
        if message.text.lower() == 'f297a57a5a743894a0e4a801fc3':
            bot.send_message(message.chat.id, 'Добро пожаловать в админ панель')
            bot.send_message(message.chat.id, 'Здесь пока ничего нет, но скоро я обязательно сяду и что-нибудь сюда добавлю ))')
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


bot.polling()

