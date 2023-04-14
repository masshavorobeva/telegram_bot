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
    global number
    global name1
    global name2
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        markup.add(btn1, btn2)
        number = message.contact.phone_number
        name1 = message.contact.first_name
        name2 = message.contact.last_name
        final_message = "Отлично!"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    count = 0
    list = []

    if get_message_bot == "1":
        count += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('')
        markup.add(btn1)
        bot.send_message(id,
                         f"Заявка {count}\nПользователь:\n{name1, name2}\nНомер:\n{number}\n{list[0]}\n{list[1]}\n{list[2]}\n{count}₽\nВариант оплаты:\nСо скидкой")
        final_message = "..."

    if get_message_bot == "2":
        count += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('')
        markup.add(btn1)
        bot.send_message(id,
                         f"Заявка {count}\nПользователь:\n{name1, name2}\nНомер:\n{number}\n{list[0]}\n{list[1]}\n{list[2]}\n{count}₽\nВариант оплаты:\nВ рассрочку")
        final_message = "..."

    if get_message_bot == "3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        final_message = "Ожидайте обратной связи"

    if get_message_bot not in [""]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button_phone = types.KeyboardButton(text="Отправить мой телефон", request_contact=True)
        markup.add(button_phone)
        final_message = "Что-то пошло не так...\nПожалуйста, жмите только на кнопки🥺.\nДавайте попробуем сначала"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)