from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tel_n = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "📞 Telfon raqam", request_contact = True)
		],
	],
	resize_keyboard = True
)

location1 = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "📍 Location", request_location = True)
		],
	],
	resize_keyboard = True
)

# advert = InlineKeyboardMarkup(
# 	inline_keyboard= [
# 		[
# 			InlineKeyboardButton(text = "Reklamani yuborish", callback_data = "rek")
# 		],
# 	]
# )

advert = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "Reklamani yuborish")
		],
	],
	resize_keyboard = True
)

fake = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Xa ✅", callback_data = "yes"),
			InlineKeyboardButton(text = "Yo'q ❌", callback_data = "no")
		],
	],
) 

# fake = ReplyKeyboardMarkup(
# 	keyboard = [
# 		[
# 			KeyboardButton(text = "Xa")
# 		],
# 	],
# 	resize_keyboard = True
# )