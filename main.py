import telebot
from telebot import types

bot = telebot.TeleBot('6891165189:AAFDgL9yrjSY3rk5Fhhmrv9mAZ7HiRePq3A')

@bot.message_handler(commands=['start'])
def welcome(message):
  welcome_message = 'Привет меня зовут Руслан и вы попали на мой скромный первый бот, здесь вы можете узнать о моих работах, обо мне и посмотреть мои фотографии, так же тут будут указанны различные контакты и соц сети, что же WELCOME 😊'

  bot.send_message(message.chat.id, f'{welcome_message}')

  # Кнопки

  btn1 = types.InlineKeyboardButton('Посмотреть на меня', callback_data='show_my_photo')
  btn2 = types.InlineKeyboardButton('Мой GitHub', url='https://github.com/GreensRoad')
  btn3 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')

  markup = types.InlineKeyboardMarkup()
  markup.row(btn1)
  markup.row(btn2, btn3)

  bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)

# Обработчики кнопок
@bot.callback_query_handler(func=lambda call: call.data == 'show_my_photo')
def send_photo(call):
  photo_path = r'C:\Users\Green\Desktop\programming\bot\images\me\me.jpg'
  chat_id = call.message.chat.id
  bot.send_photo(chat_id, photo=open(photo_path, 'rb'), caption = 'Вот это я 😄')

bot.polling(non_stop=True)