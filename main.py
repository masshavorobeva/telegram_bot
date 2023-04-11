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
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        markup.add(btn1, btn2)
        # number = message.contact.phone_number
        # name1 = message.contact.first_name
        # name2 = message.contact.last_name
        final_message = "Отлично!"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)