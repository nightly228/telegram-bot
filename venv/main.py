import telebot
from telebot import types

bot = telebot.TeleBot('7846130427:AAHt5Whc5HOdxDS2DRjmw34ltLIrpsr_3o8')

@bot.message_handler(content_types=['start']) #декоратор
def main(message):
    #bot.send_message(message.chat.id, 'Доброго времени суток!'
                                      #' Этот бот поможет Вам с выбором эко-подарка и поможет узнать что-то новое, оставайтесь с нами!'
                                      #' Вот список возможных команд:')
    #file = open('.\kk.jpeg', 'rb')
    #bot.send_photo(message.chat.id, file)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.KeyboardButton('Наличие')
    btn2 = types.KeyboardButton('Под заказ')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Интересные факты')
    markup.row(btn3)


@bot.message_handler(commands=['help','помощь','инфо']) #декоратор
def main(message):
    bot.send_message(message.chat.id, 'Доброго времени суток!'
                                      ' Этот бот поможет Вам с выбором эко-подарка и поможет узнать что-то новое, оставайтесь с нами!'
                                      ' Вот список возможных команд:')


bot.polling(none_stop=True)
