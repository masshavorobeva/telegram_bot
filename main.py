import telebot
from telebot import types


bot = telebot.TeleBot('6263372113:AAGRZDGb85N1tgQQtLLT9Sgn2KNKrtxggZA')
count = 0
spis = []
fil = 0
chet = 0
number = []
name1 = []
name2 = []
inf = []

@bot.message_handler(commands=['start'])
def start(message):
    global spis
    global number
    global name1
    global name2
    global inf
    inf = []
    name1 = []
    name2 = []
    number = []
    spis = []
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_phone = types.KeyboardButton(text="Отправить мой телефон", request_contact=True)
    markup.add(button_phone)

    send_mess = f'<b> Здравствуйте, {message.from_user.first_name} </b>!👋\nЭтот бот поможет подобрать вам классную футболку\nДля того чтобы оформить заказ нам потребуется ваш номер телефона.'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def contact(message):
    global number
    global name1
    global name2
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Я парень')
        btn2 = types.KeyboardButton('Я девушка')
        markup.add(btn1, btn2)
        number = message.contact.phone_number
        name1 = message.contact.first_name
        name2 = message.contact.last_name
        final_message = "Отлично!\nДавайте определимся с полом"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def mess(message):
    global spis
    global chet
    global number
    global name1
    global name2
    global inf
    get_message_bot = message.text.strip().lower()

    
    if get_message_bot == "я девушка":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('S')
        btn2 = types.KeyboardButton('M')
        btn3 = types.KeyboardButton('L')
        btn4 = types.KeyboardButton('XL')
        markup.add(btn1, btn2, btn3, btn4)
        file = open('Razmer.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        final_message = "Какой у вас размер?"

    if get_message_bot == "я парень":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('S')
        btn2 = types.KeyboardButton('M')
        btn3 = types.KeyboardButton('L')
        btn4 = types.KeyboardButton('XL')
        markup.add(btn1, btn2, btn3, btn4)
        file = open('Razmer.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        final_message = "Какой у вас размер?"

    if get_message_bot == "s":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('🔴')
        btn2 = types.KeyboardButton('🟡')
        btn3 = types.KeyboardButton('🟢')
        btn4 = types.KeyboardButton('🔵')
        btn5 = types.KeyboardButton('⚫️')
        btn6 = types.KeyboardButton('⚪️')
        btn7 = types.KeyboardButton('🟣')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "Какой цвет вы предпочитаете?"

    if get_message_bot == "m":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('🔴')
        btn2 = types.KeyboardButton('🟡')
        btn3 = types.KeyboardButton('🟢')
        btn4 = types.KeyboardButton('🔵')
        btn5 = types.KeyboardButton('⚫️')
        btn6 = types.KeyboardButton('⚪️')
        btn7 = types.KeyboardButton('🟣')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "Какой цвет вы предпочитаете?"

    if get_message_bot == "l":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('🔴')
        btn2 = types.KeyboardButton('🟡')
        btn3 = types.KeyboardButton('🟢')
        btn4 = types.KeyboardButton('🔵')
        btn5 = types.KeyboardButton('⚫️')
        btn6 = types.KeyboardButton('⚪️')
        btn7 = types.KeyboardButton('🟣')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "Какой цвет вы предпочитаете?"

    if get_message_bot == "xl":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('🔴')
        btn2 = types.KeyboardButton('🟡')
        btn3 = types.KeyboardButton('🟢')
        btn4 = types.KeyboardButton('🔵')
        btn5 = types.KeyboardButton('⚫️')
        btn6 = types.KeyboardButton('⚪️')
        btn7 = types.KeyboardButton('🟣')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "Какой цвет вы предпочитаете?"

    if get_message_bot == "🔴":
        inf.append(get_message_bot)
        spis.append('red')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🟡":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🟢":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🔵":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "⚫️":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "⚪️":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🟣":
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "нет":
        inf.append('Принта нет')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('К оформлению')
        markup.add(btn1)
        final_message = "Окей. Ваша футболка выглядит так?"

    if get_message_bot == "да":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Аниме')
        btn2 = types.KeyboardButton('Игры')
        btn3 = types.KeyboardButton('К пацанами')
        markup.add(btn1, btn2, btn3)
        final_message = "В каком стиле должен быть ваш принт?"

    if get_message_bot == "аниме":
        inf.append('Принт с Аниме')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        markup.add(btn1)
        final_message = "Хорошо. Ваша футболка будет выглядеть вот так"
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)

    if get_message_bot == "buhs":
        inf.append('Принт с Аниме')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        markup.add(btn1)
        final_message = "Хорошо. Ваша футболка будет выглядеть вот так"
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)

    if get_message_bot == "к пацанам":
        inf.append('Принт с пацанами')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        markup.add(btn1)
        final_message = "Хорошо. Ваша футболка будет выглядеть вот так"
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('odnot/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)


    if get_message_bot == "к оформлению":
        chet += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('К оформлению')
        markup.add(btn1)
        bot.send_message(id, f"Заявка {chet}\nПользователь:\n{name1, name2}\nНомер:\n{number}\n{inf[0]}\n{inf[1]}\n{inf[2]}")
        final_message = "Окей. Ваша футболка выглядит так?"
