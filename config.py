import telebot
from telebot import types

letters = {'3':('Б', 'В', 'Г'), '4':('А', 'В'), '5':('А', 'Б'), '6':('А', 'Б', 'И'),
           '7':('А', 'Б', 'Е(ен/г)', 'К', 'Л', 'М', 'Т'), '8':('Г', 'Е', 'М', 'Т'),
           '9':('А', 'Б', 'М'), '10':('А(медиа)', 'А(унив)', 'И(инж)', 'И(it)', 'К(соц-эк)', 'К(хим-био)'),
           '11':('А', 'Б(инж)', 'Б(соц-эк)', 'Б(хим-био)', 'Б(унив)', 'В(1)', 'В(2)')}

token = '1348485436:AAGE2oXJ6uxAHwHRaaagEJUZK7_Mz547N1E'
token_old = '1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY'

kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

kb_cookie = telebot.types.ReplyKeyboardMarkup(True, True)
kb_cookie.row('Дать печеньку', 'Выйти')

kb_admc = telebot.types.ReplyKeyboardMarkup(True, True)
kb_admc.row('Создать новую запись', 'Удалить запись').add('Просмотреть все записи', 'Выйти')

kb_adm_table = telebot.types.ReplyKeyboardMarkup(True, True)
kb_adm_table.row('math', 'phys', 'inf')

kb_yes_no = telebot.types.ReplyKeyboardMarkup(True, True)
kb_yes_no.row('Да', 'Нет')

kb_fb = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fb.row('Жалоба', 'Предложение')

kb_ask = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask.row('Просмотреть список доступных вопросов', 'Написать вручную')

kb_ask_t = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask_t.row('Математика', 'Физика', 'Информатика')

kb_test = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test.row('Математика', 'Физика', 'Информатика', 'Выход')

kb_test_qty = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test_qty.row('5', '7', '10', '15')

kb_test_mistakes = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test_mistakes.row('Просмотреть ошибки', 'Выйти')

kb_test_end = types.InlineKeyboardMarkup(row_width=2)
kb_test_end_ = types.InlineKeyboardButton(text="Закончить прохождение теста", callback_data="end")
kb_test_end.add(kb_test_end_)

adm = 'f297a57a5a743894a0e4a801fc3'

