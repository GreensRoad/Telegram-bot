import telebot
from telebot import types

bot = telebot.TeleBot('6891165189:AAFDgL9yrjSY3rk5Fhhmrv9mAZ7HiRePq3A')

@bot.message_handler(commands=['start'])
def welcome(message):
  welcome_message = 'Привет меня зовут Руслан и вы попали на мой скромный первый бот, здесь вы можете узнать о моих работах, обо мне и посмотреть мои фотографии, так же тут будут указанны различные контакты и соц сети, что же WELCOME =)'

  bot.send_message(message.chat.id, f'{welcome_message}')

  # Кнопки

  btn1 = types.InlineKeyboardButton('Посмотреть на меня', url='https://google.com')
  btn2 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
  btn3 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')

  markup = types.InlineKeyboardMarkup()
  markup.row(btn1)
  markup.row(btn2, btn3)

  bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


bot.polling(non_stop=True)