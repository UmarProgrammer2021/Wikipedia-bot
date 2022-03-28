import logging
import wikipedia

from aiogram import Bot,Dispatcher,executor,types

API_TOKEN='5156224883:AAHWd4M2v_sFO40xICiYEJ3BVg2Xee1zbGw'

wikipedia.set_lang('UZ')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# dp misol uchun bu Telebotagi client ozgaruvchisiga oxshagan bir ozgaruvchi

@dp.message_handler(commands=['/start','/about'])
async def send_welcome(message:types.Message):
    #Bu start bosganda javob beradi
    await message.reply('Wikipediya botiga hush kelibsiz')
    
@dp.message_handler()
async def sendWiki(message:types.Message):
    try:
        respon=wikipedia.summary(message.text)
        await message.answer(respon)
    except:
        await message.asnwer('Bunday mallumot topilmadi')
    
    #Bu foydalanuvchi yazgan textni olib bizga qaytishi uchun
    #await message.answer(message.text)
    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)