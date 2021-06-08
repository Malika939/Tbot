import telebot
from telebot.types import Message
import config
import random


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
  sti = open("static/AnimatedSticker.tgs", "rb")
  bot.send_sticker(message.chat.id, sti)


  markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = telebot.types.KeyboardButton("👍Рандомное число")
  item2 = telebot.types.KeyboardButton("Хочу купить компьютер")
  markup.add(item1, item2)

  bot.send_message(message.chat.id, 
    '''Добро пожаловать {0.first_name}! 
    Я {1.first_name}, бот, который тебя приветствует'''.format(
      message.from_user, 
      bot.get_me()), 
      parse_mode='html', 
      reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
  if message.chat.type == 'private':
    if message.text == "👍Рандомное число":
      bot.send_message(message.chat.id, 
        str(random.randint(1, 1000000)))
    elif message.text == "Хочу купить компьютер":


      markup = telebot.types.InlineKeyboardMarkup(row_width=2)
      item1 = telebot.types.InlineKeyboardButton("Ноутбук", callback_data='good')
      item2 = telebot.types.InlineKeyboardButton("Стационарный", callback_data='good')
      markup.add(item1, item2)

      bot.send_message(message.chat.id,
        "Какой ноутбук вас интересует?", reply_markup=markup)
    else:
      bot.send_message(message.chat.id,
        "Я не знаю что ответить")




@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
  try:
    if call.message:
      if call.data == 'good':
        bot.send_message(call.message.chat.id, "Можем предложить Макбуки")

        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton("Да, пожалуйста", callback_data='yes')
        item2 = telebot.types.InlineKeyboardButton("Нет, сам разберусь", callback_data='yes')
        markup.add(item1, item2)

        bot.send_message(call.message.chat.id,
        "Соориентировать вас по цене?", reply_markup=markup)
        

      if call.data == 'yes':
        if call.message:
          if call.data == 'yes':
            bot.send_message(call.message.chat.id, "Хорошо")


            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("Про", callback_data='pro')
            item2 = telebot.types.InlineKeyboardButton("Эйр", callback_data='air')
            markup.add(item1, item2)

            bot.send_message(call.message.chat.id,
            "Вам Про или эйр?", reply_markup=markup)

            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
          )

      if call.data == 'pro':
        if call.message:
          if call.data == 'pro':
            bot.send_message(call.message.chat.id, "Отличный выбор")


            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("16", callback_data='16')
            item2 = telebot.types.InlineKeyboardButton("32", callback_data='32')
            markup.add(item1, item2)

            bot.send_message(call.message.chat.id,
            "Вам Про на 16 или 32 Gb?", reply_markup=markup)

            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
            )

      elif call.data == 'air':
        bot.send_message(call.message.chat.id, "С вас 85000, перейдите к кассе")
      
      if call.data == '16':
        if call.message:
          if call.data == '16':
            bot.send_message(call.message.chat.id, "Отличный выбор")

            bot.send_message(call.message.chat.id,
            "С вас 125000, перейдите к кассе")

            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
            )
      elif call.data == '32':
        bot.send_message(call.message.chat.id, "С вас 150000, перейдите к кассе")

        bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
      )   

  except Exception as e:
    print(e)


bot.polling(none_stop=True)