import telebot
from telebot import types


bot = telebot.TeleBot('5888347857:AAHyqkDGKk5EuW-otOrjso30Z-qub4pzuUo')
spis = []
chet = 0
number = []
name1 = []
name2 = []
inf = []
nik = []

@bot.message_handler(commands=['start'])
def start(message):
    global spis
    global number
    global name1
    global name2
    global inf
    global nik
    nik = []
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
    global nik
    if message.contact is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Я парень')
        btn2 = types.KeyboardButton('Я девушка')
        markup.add(btn1, btn2)
        number = message.contact.phone_number
        name1 = message.contact.first_name
        name2 = message.contact.last_name
        nik = message.from_user.username
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
    global nik
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "я девушка":
        inf.append('Девушка')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('S')
        btn2 = types.KeyboardButton('M')
        btn3 = types.KeyboardButton('L')
        btn4 = types.KeyboardButton('XL')
        markup.add(btn1, btn2, btn3, btn4)
        file = open('size.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        final_message = "Какой у вас размер?"

    if get_message_bot == "я парень":
        inf.append('Парень')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('S')
        btn2 = types.KeyboardButton('M')
        btn3 = types.KeyboardButton('L')
        btn4 = types.KeyboardButton('XL')
        markup.add(btn1, btn2, btn3, btn4)
        file = open('size.jpg', 'rb')
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
        spis.append('yellow')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🟢":
        spis.append('green')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🔵":
        spis.append('blue')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "⚫️":
        spis.append('black')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "⚪️":
        spis.append('white')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "🟣":
        spis.append('purple')
        inf.append(get_message_bot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        final_message = "Хотите ли вы принт на свое футболке?"

    if get_message_bot == "нет":
        inf.append('Принта нет')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        btn2 = types.KeyboardButton('Изменить выбор')
        markup.add(btn1, btn2)
        final_message = "Коллекция: Spring 2023 - Summer 2023\nСостав: 100% хлопок\nСтиль: Повседневный\nСилует: Свободный\n<b>Цена: 999 рублей</b>"
        if 'red' in spis:
            file = open('color/red.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'blue' in spis:
            file = open('color/blue.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'black' in spis:
            file = open('color/black.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'white' in spis:
            file = open('color/white.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'yellow' in spis:
            file = open('color/yellow.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'purple' in spis:
            file = open('color/purple.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'green' in spis:
            file = open('color/green.jpg', 'rb')
            bot.send_photo(message.chat.id, file)

    if get_message_bot == "да":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Аниме')
        btn2 = types.KeyboardButton('Корейцы')
        btn3 = types.KeyboardButton('Дрилл')
        markup.add(btn1, btn2, btn3)
        final_message = "В каком стиле должен быть ваш принт?"

    if get_message_bot == "дрилл":
        inf.append('Принт с мемами')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        btn2 = types.KeyboardButton('Изменить выбор')
        markup.add(btn1, btn2)
        final_message = "Коллекция: Spring 2023 - Summer 2023\nСостав: 100% хлопок\nСтиль: Повседневный\nСилует: Свободный\n<b>Цена: 1299 рублей</b>"
        if 'blue' in spis:
            file = open('drill/blue3.jpeg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('drill/red3.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'green' in spis:
            file = open('drill/green3.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'black' in spis:
            file = open('drill/black3.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'purple' in spis:
            file = open('drill/purple3.jpeg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'yellow' in spis:
            file = open('drill/yellow3.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'white' in spis:
            file = open('drill/white3.jpeg', 'rb')
            bot.send_photo(message.chat.id, file)

    if get_message_bot == "аниме":
        inf.append('Принт с Аниме')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        btn2 = types.KeyboardButton('Изменить выбор')
        markup.add(btn1, btn2)
        final_message = "Коллекция: Spring 2023 - Summer 2023\nСостав: 100% хлопок\nСтиль: Повседневный\nСилует: Свободный\n<b>Цена: 1299 рублей</b>"
        if 'blue' in spis:
            file = open('anime/blue_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'red' in spis:
            file = open('anime/red_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'green' in spis:
            file = open('anime/green_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'black' in spis:
            file = open('anime/black_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'purple' in spis:
            file = open('anime/purple_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'yellow' in spis:
            file = open('anime/yellow_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'white' in spis:
            file = open('anime/white_anime.jpg', 'rb')
            bot.send_photo(message.chat.id, file)

    if get_message_bot == "корейцы":
        inf.append('Принт с Корейцами')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Заказать')
        btn2 = types.KeyboardButton('Изменить выбор')
        markup.add(btn1, btn2)
        final_message = "Коллекция: Spring 2023 - Summer 2023\nСостав: 100% хлопок\nСтиль: Повседневный\nСилует: Свободный\n<b>Цена: 1299 рублей</b>"
        if 'red' in spis:
            file = open('korean/red2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'blue' in spis:
            file = open('korean/blue2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'green' in spis:
            file = open('korean/green2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'white' in spis:
            file = open('korean/white2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'yellow' in spis:
            file = open('korean/yellow2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'black' in spis:
            file = open('korean/black2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
        if 'purple' in spis:
            file = open('korean/purple2.jpg', 'rb')
            bot.send_photo(message.chat.id, file)


    if get_message_bot == "заказать":
        chet += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bot.send_message(731746986, f"Заявка {chet}\nПользователь:\n{name1, name2}\nНомер:\n+{number}\n@{nik}\n\n{inf[0]}\nРазмер:{inf[1]}\nЦвет - {inf[2]}\n{inf[3]}")
        final_message = "Благодарим за использвание нашего телеграм бота.\nВаш заказ уже находится на рассмотрении.\nВ скором времени с вами свяжуться для уточнения деталей.Ожидайте обратной связи"

    if get_message_bot not in ["заказать", "дрилл", "корейцы", "аниме", "да", "нет", "🟣", "⚪️","⚫️", "🔵", "🟢", "🟡", "🔴", "xl", "l", "m", "s", "я парень", "я девушка"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button_phone = types.KeyboardButton(text="Отправить мой телефон", request_contact=True)
        markup.add(button_phone)
        final_message = "Что-то пошло не так...\nПожалуйста, жмите только на кнопки🥺.\nДавайте попробем сначала"

    if get_message_bot == "изменить выбор":
        spis = []
        inf = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Я парень')
        btn2 = types.KeyboardButton('Я девушка')
        markup.add(btn1, btn2)
        final_message = "Отлично!\nДавайте определимся с полом"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)