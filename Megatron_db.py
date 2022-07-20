import telebot
from telebot import types

bot = telebot.TeleBot('5575999917:AAHRxmw7QnAQ1a8qJd-TR3YSOIOM52GFNps')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎬 Фильмы")
    btn2 = types.KeyboardButton("😊 Мультфильмы")
    btn3 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id,
                     text="👋 Привет, {0.first_name}! Я тестовый бот, ты можешь выбрать для себя что-то ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🎬 Фильмы"):
        bot.send_message(message.chat.id, text=" Фильмы из этого жанра :"
                                               "\n✔️Смерть на Ниле"
                                               "\n✔️Клон"
                                               "\n✔️Бэтмен"
                                               "\n✔️Человек-паук"
                                               "\n✔️Ночь в музеи"
                                               "\n✔️Девять жизней"
                                               "\n✔️Гонка со временем"
                                               "\n✔️Черный телефон"
                                               "\n✔️Флешбэк"
                                               "\n✔️Мир Юрского периода"
                                               "\n✔️Анамат")

    elif (message.text == "😊 Мультфильмы"):
        bot.send_message(message.chat.id, text="Мультфильмы из этого жанра :"
                                               "\n✔️Миньоны"
                                               "\n✔️Смешарики"
                                               "\n✔️Фиксики"
                                               "\n✔️Сказачный патруль"
                                               "\n✔️Леди-Баг и Супер кот"
                                               "\n✔️Три богатрыря"
                                               "\n✔️Алладин"
                                               "\n✔️Ну, погоди !"
                                               "\n✔️Три кота"
                                               "\n✔️Рапунцель"
                                               "\n✔️Соник")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔥Топ")
        btn2 = types.KeyboardButton("🎥Жанры")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "🔥Топ"):
        bot.send_message(message.chat.id,  text=" Топ фильмов :"
                                                "\n✔️Побег из Шоушенка"
                                               "\n✔️Унесенные призраками"
                                               "\n✔️Паразиты"
                                               "\n✔️Темный рыцарь"
                                               "\n✔️Криминальное чтиво"
                                               "\n✔️Властелин колец"
                                               "\n✔Легенда о волках"
                                               "\n✔Психо"
                                               "\n✔Город бога"
                                               "\n✔Ее заветное желание")
    elif (message.text == "🎥Жанры"):
        bot.send_message(message.chat.id, text=" Выберете жанр:"
                                                "\nБоевик"
                                               "\n✔Приключения"
                                               "\n✔Ужасы"
                                               "\n✔Комедии"
                                               "\n✔Вестерн"
                                               "\n✔Драма"
                                               "\n✔Семейные"
                                               "\n✔Криминал"
                                               "\n✔Военный"
                                               "\n✔Фантастика")


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🎬 Фильмы")
        button2 = types.KeyboardButton("😊 Мультфильмы")
        button3 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2,button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, f'👋 До новых встреч, {message.from_user.first_name}')
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)


