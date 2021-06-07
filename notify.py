import telebot
import requests
import datetime
import jsons
import firebase_admin
from firebase_admin import credentials , firestore
import time
import schedule
import config


firebase_admin.initialize_app(cred)
db = firestore.client()
bot = telebot.TeleBot(token=token)
NOTIFY = False
id1 = config.id1
qq = config.qq
DISTRICT_CODE = config.DISTRICT_CODE

# ///////////////////////////////////////////////////////////////////////////////////////////////////


def get_date(this):
	global date_got
	x = datetime.date.today()+ datetime.timedelta(days = this) 
	day = str(x.day).zfill(2)
	month = str(x.month).zfill(2)
	year = str(x.year).zfill(2)
	y = [day , month , year]
	date_got = str("-".join(y))
	return date_got


def making_request_dating(RequestDate):
	global list_sessions
	url1 = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={DISTRICT_CODE}&date="
	url = url1 + RequestDate
	# print(url)
	head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
	head1 = {"User-Agent":"Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0"}
	response = requests.get(url , headers=head1)
	data = response.json()
	l = jsons.load(data)
	a = l["sessions"]
	list_sessions = []
	for i in a:
		if i["available_capacity"] != 0:
			lst = []
			name = i["name"] 
			address = i["address"]
			# city = i["district_name"]
			date_new = i["date"]
			fee_new = i["fee_type"]
			fee = i["fee"]
			if fee_new == "Paid":
				fee_new = fee_new+" ( "+fee+" )"
			dose1 = i["available_capacity_dose1"]
			dose2 = i["available_capacity_dose2"]
			age_min = i["min_age_limit"]
			vaccine = i["vaccine"]
			tot_dose = i["available_capacity"]
			lst.append(name)
			lst.append(address)
			# lst.append(city)
			lst.append(fee_new)
			lst.append(date_new)
			lst.append(vaccine)
			lst.append(age_min)			
			lst.append(dose1)
			lst.append(dose2)
			lst.append(tot_dose)
			if tot_dose != 0:
				list_sessions.append(lst)
			# print(list_sessions)


def making_request(RequestDate):
	global list_sessions
	url1 = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={DISTRICT_CODE}&date="
	url = url1 + RequestDate
	head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
	head1 = {"User-Agent":"Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0"}
	# print(url)
	response = requests.get(url , headers=head1)
	data = response.json()
	l = jsons.load(data)
	a = l["centers"]
	list_sessions = []
	for i in a:
		name = i["name"] 
		address = i["address"]
		fee_new = i["fee_type"]
		if fee_new == "Paid":
			w = i["vaccine_fees"]
			for qq in w:
				fee = qq["fee"]
			fee_new = fee_new+" ( "+fee+" )"
		b = i["sessions"]
		z = b[0]
		if z["available_capacity"] != 0 :
			bg_list = []
			datet = z["date"]
			vaccine = z["vaccine"]
			age = z["min_age_limit"]
			dose1 = z["available_capacity_dose1"]
			does2 = z["available_capacity_dose2"]
			bg_list.append(name)
			bg_list.append(address)
			bg_list.append(fee_new)
			bg_list.append(datet)
			bg_list.append(vaccine)
			bg_list.append(age)
			bg_list.append(dose1)
			bg_list.append(does2)
			bg_list.append(z["available_capacity"])
			list_sessions.append(bg_list)
			# print(bg_list , f"\n")


# ///////////////////////////////////////////////////////////////


def t18_dating(this):
	global t18_text
	data_18 = []
	making_request_dating(get_date(this))
	t18_text = []
	# print(list_sessions)
	for i in list_sessions:
			# print(i)
			if i[5] == 18:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*\nUrl : https://selfregistration.cowin.gov.in/'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				t18_text.append(l)
				# print(l)


def t45_dating(this):
	global t45_text
	data_45 = []
	making_request_dating(get_date(this))
	t45_text = []
	# print(list_sessions)
	for i in list_sessions:
			# print(i)
			if i[5] == 45:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*\nUrl : https://selfregistration.cowin.gov.in/'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				t45_text.append(l)
				# print(l)


def t18_get(this):
	global t18_text
	data_18 = []
	making_request(get_date(this))
	t18_text = []
	# print(list_sessions)
	for i in list_sessions:
			# print(i)
			if i[5] == 18:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*\nUrl : https://selfregistration.cowin.gov.in/'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				t18_text.append(l)
				# print(l)


def t45_get(this):
	global t45_text
	data_45 = []
	making_request(get_date(this))
	t45_text = []
	for i in list_sessions:
			if i[5] == 45:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*\nUrl : https://selfregistration.cowin.gov.in/'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				t45_text.append(l)
				# print(l)


# /////////////////////////////////////////////////////


def check_dating_18():
	for this in range(3):
		t18_dating(this)
		min_num = 50
		print("18...")
		# print(t18_text)
		for i in t18_text:
			print(i)
		print("\n")
		for i in t18_text:
			try:
				doc = db.collection("18plus").document(str(i[1]) + str(i[3]))
				a = doc.get().to_dict()
				c = int(a.get("total_dose"))
				d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)

			except:
				if i[2]>min_num:
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					doc = db.collection("18plus").document(str(i[1]) + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})


def check_dating_45():
	for this in range(3):
		t45_dating(this)
		min_num = 50
		print("45...")
		# print(t45_text)
		for i in t45_text:
			print(i)
		print("\n")
		for i in t45_text:
			try:
				doc = db.collection("45plus").document(str(i[1]) + str(i[3]))
				a = doc.get().to_dict()
				c = int(a.get("total_dose"))
				d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)

			except:
				if i[2]>min_num:
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					doc = db.collection("45plus").document(str(i[1]) + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})


def check_18():
	for this in range(6):
		t18_dating(this)
		min_num = 50
		print("18...")
		# print(t18_text)
		for i in t18_text:
			print(i)
		print("\n")
		for i in t18_text:
			try:
				doc = db.collection("18plus").document(str(i[1]) + str(i[3]))
				a = doc.get().to_dict()
				c = int(a.get("total_dose"))
				d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)

			except:
				if i[2]>min_num:
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					doc = db.collection("18plus").document(str(i[1]) + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})


def check_45():
	for this in range(6):
		t45_get(this)
		min_num = 50
		print("45...")
		# print(t45_text)
		for i in t45_text:
			print(i)
		print("\n")
		for i in t45_text:
			try:
				doc = db.collection("45plus").document(str(i[1]) + str(i[3]))
				a = doc.get().to_dict()
				c = int(a.get("total_dose"))
				d = str(a.get("date"))
				if (c < i[2]) and (i[2] > min_num):
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)

			except:
				if i[2]>min_num:
					bot.send_message( qq,i[0],parse_mode ="Markdown")
					doc = db.collection("45plus").document(str(i[1]) + str(i[3]))
					doc.set({"date" : i[3] , "total_dose" : i[2]})



# ///////////////////////////////////////////////////


@bot.message_handler(commands=["notify_start"])
def send_welcome(message):
	global NOTIFY
	NOTIFY = False
	min_num = 50
	print("Started notify")
	if message.from_user.id == id1 :
		# try:
			id = message.from_user.id
			bot.send_message( id , "Started NOTIFY")
			NOTIFY = True
			schedule.every(20).seconds.do(check_dating_18)
			schedule.every(20).seconds.do(check_dating_45)
			schedule.every(20).seconds.do(check_18)
			schedule.every(20).seconds.do(check_45)
			while NOTIFY == True:
				schedule.run_pending()
				time.sleep(1)
		# except:
			# bot.send_message(id, "Failed to start")



@bot.message_handler(commands=["notify_stop"])
def send_welcome(message):
	global NOTIFY
	if message.from_user.id == id1 :
		try:
			NOTIFY = False
			schedule.cancel_job(check_dating_18())
			schedule.cancel_job(check_dating_45())
			schedule.cancel_job(check_18())
			schedule.cancel_job(check_45())
			bot.send_message( id1 , "Stopped NOTIFY")
			print("Stopped notify")

		except:
			bot.send_message( id1 , "Failed To stop")


# /////////////////////////////////////////////////////////////




while True:
	print("started...")
	bot.polling()