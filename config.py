import telebot

token = '1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY'

kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

kb_admc = telebot.types.ReplyKeyboardMarkup(True, True)
kb_admc.row('Создать новую запись в БД','Удалить запись из БД').add('Просмотреть все записи', 'Выйти')

kb_adm = telebot.types.ReplyKeyboardMarkup(True, True)
kb_adm.row('/adm')

kb_yes_no = telebot.types.ReplyKeyboardMarkup(True, True)
kb_yes_no.row('Да', 'Нет')

adm = 'f297a57a5a743894a0e4a801fc3'
