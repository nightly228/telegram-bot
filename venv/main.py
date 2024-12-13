from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = telebot.TeleBot('7846130427:AAHt5Whc5HOdxDS2DRjmw34ltLIrpsr_3o8')

@bot.message_handlers(commands=['start']) #декоратор
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyBoardButton('Открыть веб-страницу', web_app=WebAppInfo(url='http://')))
    await message.answer('Привет', reply_markup=markup)



executor.start_polling(dp)
