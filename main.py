import telebot
from telebot import types


bot = telebot.TeleBot('id')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_phone = types.KeyboardButton(text="Отправить мой телефон", request_contact=True)
    markup.add(button_phone)

    send_mess = f'<b> Здравствуйте, {message.from_user.first_name} </b>!👋\n\nЭтот бот....'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact(message):