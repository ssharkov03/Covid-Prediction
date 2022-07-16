import telebot
from main import graph_map
from main import check_flag
import main
bot = telebot.TeleBot('5416009013:AAEJCgFVQbyBMXYIersiftQYG70zTIexNQA')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Россия', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Сибирский',callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Приволжский', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Южный', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Уральский', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='Дальневосточный', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Центральный', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='Северо-Западный', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='Северо-Кавказский', callback_data=9))
    bot.send_message(message.chat.id, text="Здравствуйте! Статистика по какому региону вас интересует?", reply_markup=markup)
    ChatId = message.chat.id
    print(ChatId)
    f = open("C:/Users/Владислав/PycharmProjects/tg_bot/text", "w")
    f.write(str(ChatId))
    f.close()
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    f = open('C:/Users/Владислав/PycharmProjects/tg_bot/text', 'r')
    chat_id = f.readline()
    bot.answer_callback_query(callback_query_id=call.id, text='ожидайте')
    answer = ''
    if call.data == '1':
        check_flag(0,'Россия')
        bot.send_document(chat_id=int(chat_id),document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '2':
        check_flag(1, 'Сибирский')
        bot.send_document(chat_id=int(chat_id),document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '3':
        check_flag(1, 'Приволжский')
        bot.send_document(chat_id=int(chat_id),document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '4':
        check_flag(1, 'Южный')
        bot.send_document(chat_id=int(chat_id),document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '5':
        check_flag(1, 'Уральский')
        bot.send_document(chat_id=int(chat_id),document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '6':
        check_flag(1, 'Дальневосточный')
        bot.send_document(chat_id=int(chat_id), document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '7':
        check_flag(1, 'Центральный')
        bot.send_document(chat_id=int(chat_id), document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '8':
        check_flag(1, 'Северо-Западный')
        bot.send_document(chat_id=int(chat_id), document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    elif call.data == '9':
        check_flag(1, 'Северо-Кавказский')
        bot.send_document(chat_id=int(chat_id), document=open('C:/Users/Владислав/PycharmProjects/tg_bot/region.html', 'rb'))
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
bot.polling(none_stop=True, interval=0)
