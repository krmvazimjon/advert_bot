import logging
# from buttons import * 
from aiogram import Bot, Dispatcher, executor, types
from configs import API_TOKEN
from aiogram.types import CallbackQuery
import sqlite3
from db import *
from buttons import *
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
admin = 913748839
base = Sql()    # class database

############ adminga xabar kelish va databse di ulash #######################################################
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    base.base_create()
    global user_id
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    data1 = base.id_user(user_id)
    if data1 is None:
        base.user_add(user_id,username,first_name)
        await message.reply("Assalom Alaykum\nTelefon raqamingizni yuboring..", reply_markup = tel_n)
    else:
        await message.answer("Siz ruyhatdan uzgansiz")

############# contact saqlash #####################
@dp.message_handler(content_types = ['contact'])
async def contact(message: types.Message):
    tel_number = message.contact['phone_number']
    base.contact_update(user_id,tel_number)
    await message.reply("Joylashuvingizni yuboring..", reply_markup = location1)

################ reklama #####################
# @dp.message_handler(commands = ['reklama'], user_id = 913748839)
# async def advert(message: types.Message):
#     base.advert(user_id)
#     x = base.advert(user_id)
#     for data in x:
#         user_id = i[0]
#         await bot.send_message(chat_id = user_id, text = f"Follow the channel https://t.me")

@dp.message_handler(commands = ['reklama'], user_id = 913748839)
async def send(message: types.Message):
    await message.reply("Kanaldi Nomi kiriting", reply_markup = advert)

@dp.message_handler(user_id = 913748839)
async def soz(message: types.Message):
    global text2 
    text2 = message.text
    await message.reply("Yuborishni Hohlaysizmi?", reply_markup = fake)
    

@dp.callback_query_handler(text = "yes",user_id = 913748839)
async def yes(call: CallbackQuery):
    await bot.send_message(chat_id = user_id, text = f"Join this Channel {text2}")

@dp.callback_query_handler(text = "no", user_id = 913748839)
async def no(call: CallbackQuery):
    await bot.send_message(admin, f"Kanal reklamaga yuborilmadi")

# ################################## reklama yuborish #####################################################################
# @dp.message_handler(commands = ['reklama'], user_id = 913748839)
# async def send_welcome(message: types.Message):
#     connection = sqlite3.connect("userinfo.db")
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM user")
#     data = cursor.fetchall()
#     for i in data:
#         user_id = i[0]
#         await bot.send_message(chat_id = user_id, text = f"Follow the channel https://t.me")

########### Lokatsiya qabul qilish #################
@dp.message_handler(content_types = ['location'])
async def contact(message: types.Message):
    cor1 = message.location.latitude
    cor2 = message.location.longitude
    base.location_update(user_id,cor1,cor2)
    z = base.admin_send(user_id)
    await message.reply("Saved")
    await bot.send_message(admin,f"Royhatdan otgan foydalanuvchi\nID: {z[0]}\nUsername: @{z[1]}")
    await bot.send_location(admin,latitude = {z[4]}, longitude = {z[5]})

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
