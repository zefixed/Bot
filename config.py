import telebot

token = '1348485436:AAETyTwfpvevMsozjXoQl9WRZptjhAwH-Ks'
token_old = '1246639039:AAGXABe2xAj33-N7Auqld5J9ZRTXa6NdtDY'

kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Привет', 'Пока')

kb_cookie = telebot.types.ReplyKeyboardMarkup(True, True)
kb_cookie.row('Дать печеньку', 'Выйти')

kb_admc = telebot.types.ReplyKeyboardMarkup(True, True)
kb_admc.row('Создать новую запись в БД', 'Удалить запись из БД').add('Просмотреть все записи', 'Выйти')

kb_admbd = telebot.types.ReplyKeyboardMarkup(True, True)
kb_admbd.row('radical_power_logarithm', 'trigonometry').add('probability_theory', 'geometric_concepts').add('algebraic_concepts')

kb_adm = telebot.types.ReplyKeyboardMarkup(True, True)
kb_adm.row('/adm')

kb_yes_no = telebot.types.ReplyKeyboardMarkup(True, True)
kb_yes_no.row('Да', 'Нет')

kb_fb = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fb.row('Проблема', 'Предложение')

kb_ask = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask.row('Просмотреть список доступных вопросов', 'Написать вручную')

kb_ask_t = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ask_t.row('Корни, степени, логарифмы', 'Тригонометрия').add('Теория вероятностей', 'Геометрические понятия').add('Алгебраические понятия и интересные вопросы')

adm = 'f297a57a5a743894a0e4a801fc3'
