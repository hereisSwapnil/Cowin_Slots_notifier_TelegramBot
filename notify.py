import telebot
import firebase_admin
from firebase_admin import credentials , firestore
from telebot import types
from settings import app_secrets
import request

# /////////////////////////////////////////////////////

firebase_admin.initialize_app(app_secrets.cred)
db = firestore.client()
bot = telebot.TeleBot(token = app_secrets.token)

# /////////////////////////////////////////////////////
 
# BUTTONS.........................

markup = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton('BOOK NOW', url = "https://selfregistration.cowin.gov.in/")
markup.add(btn)

# ///////////////////////////////////////////////////////////////////////////////////////////////////

Personal_Notify_Ids = [12345]

PERSONAL_SEND_AGE = 18

PERSONAL_SEND_DATE = ["dd/mm/yyyy"]

PERSONAL_SEND_VACCINE = "COVAXIN/COVISHEILD"

PERSONAL_RUN = True

# ///////////////////////////////////////////////////////////////////////////////////////////////////

def personal_notify(vaccine , date , text , age):
	if vaccine == PERSONAL_SEND_VACCINE and date in PERSONAL_SEND_DATE and age == PERSONAL_SEND_AGE:
		for i in owner:
			bot.send_message( i , text ,parse_mode ="Markdown")

# /////////////////////////////////////////////////////

SEND_18PLUS_group = True
SEND_45PLUS_group = True

def text_18_one(this):
	global t18_text
	data_18 = []
	imports.request.request_one(config.requests.get_date(this))
	t18_text = []
	for i in list_sessions:
			if i[5] == 18:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t18_text.append(l)


def text_18_two(this):
	global t18_text
	data_18 = []
	imports.request.request_two(config.requests.get_date(this))
	t18_text = []
	for i in list_sessions:
			if i[5] == 18:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t18_text.append(l)


def text_45_one(this):
	global t45_text
	data_45 = []
	imports.request.request_one(config.requests.get_date(this))
	t45_text = []
	for i in list_sessions:
			if i[5] == 45:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t45_text.append(l)


def text_45_two(this):
	global t45_text
	data_45 = []
	imports.request.request_two(config.requests.get_date(this))
	t45_text = []
	for i in list_sessions:
			if i[5] == 45:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t45_text.append(l)

# /////////////////////////////////////////////////////

minimum_doses_under_18 = 40
minimum_doses_above_45 = 30
number_of_days_check_18 = 4
number_of_days_check_45 = 4

def send_18_one():
	for this in range(number_of_days_check_18):
		text_18_one(this)
		for i in t18_text:
			try:
				if (i[2] > minimum_doses_under_18):
					doc = db.collection("18plus").document(str(i[1]) +i[4] + str(i[3]))
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c < i[2]) and (i[2] > minimum_doses_under_18):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_18PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0] , i[5])

			except:
				if i[2]>minimum_doses_under_18:
					doc = db.collection("18plus").document(str(i[1]) + i[4] +str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_18PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

def send_18_two():
	for this in range(number_of_days_check_18):
		send_18_two(this)
		for i in t18_text:
			try:
				if (i[2] > minimum_doses_under_18):
					doc = db.collection("18plus").document(str(i[1]) +i[4] +str(i[3]))
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_18PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_under_18:
					doc = db.collection("18plus").document(str(i[1]) +i[4] + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_18PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

def send_45_one():
	for this in range(number_of_days_check_45):
		send_45_one(this)
		for i in t45_text:
			try:
				if (i[2] > minimum_doses_above_45):
					doc = db.collection("45plus").document(str(i[1]) + i[4] +str(i[3]))
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c < i[2]) and (i[2] > minimum_doses_above_45):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_45PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_above_45:
					doc = db.collection("45plus").document(str(i[1]) +i[4] + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_45PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

def send_45_two():
	for this in range(number_of_days_check_45):
		t45_dating(this)
		for i in t45_text:
			try:
				if (i[2] > minimum_doses_above_45):
					doc = db.collection("45plus").document(str(i[1]) + i[4] +str(i[3]))
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					print("2")
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_45PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_above_45:
					doc = db.collection("45plus").document(str(i[1]) + i[4] +str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_45PLUS_group:
						bot.send_message( app_secrets.Telegram_Groupid,i[0],parse_mode ="Markdown",reply_markup = markup)
					print(i[0])
					if PERSONAL_RUN:
						personal_notify(i[4] , i[3] , i[0], i[5])

# /////////////////////////////////////////////////////
run_times = 0
def RUN():
	if SEND_18PLUS_group or PERSONAL_RUN and PERSONAL_SEND_AGE == 18 :
		send_18_one()
		send_18_two()
	if SEND_45PLUS_group or PERSONAL_RUN and PERSONAL_SEND_AGE == 45 :
		send_45_one()
		send_45_two()

