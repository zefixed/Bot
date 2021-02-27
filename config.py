import telebot
from telebot import types

token = '1348485436:AAHMeMOVAXSfgVaA0208oy5cdRUGWIN0pIg'
token_old = '1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY'

kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

kb_cookie = telebot.types.ReplyKeyboardMarkup(True, True)
kb_cookie.row('Дать печеньку', 'Выйти')

kb_admc = telebot.types.ReplyKeyboardMarkup(True, True)
kb_admc.row('Создать новую запись', 'Удалить запись').add('Просмотреть все записи', 'Выйти')

kb_adm_table = telebot.types.ReplyKeyboardMarkup(True, True)
kb_adm_table.row('math')

kb_adm = telebot.types.ReplyKeyboardMarkup(True, True)
kb_adm.row('/adm')

kb_yes_no = telebot.types.ReplyKeyboardMarkup(True, True)
kb_yes_no.row('Да', 'Нет')

kb_fb = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fb.row('Проблема', 'Предложение')

kb_ask = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask.row('Просмотреть список доступных вопросов', 'Написать вручную')

kb_ask_t = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask_t.row('Математика')

kb_test = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test.row('Математика', 'Выход')

kb_test_qty = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test_qty.row('5', '7', '10', '15')

kb_test_mistakes = telebot.types.ReplyKeyboardMarkup(True, True)
kb_test_mistakes.row('Просмотреть ошибки', 'Выйти')

kb_test_end = types.InlineKeyboardMarkup(row_width=2)
kb_test_end_ = types.InlineKeyboardButton(text="Закончить прохождение теста", callback_data="end")
kb_test_end.add(kb_test_end_)

adm = 'f297a57a5a743894a0e4a801fc3'

