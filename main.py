import bot
from settings import app_secrets
import time
import datetime as dt
from datetime import datetime
import os
import notify
import centre_schedule_scrapper

def current_date():
	now = dt.now()
	dt_string = now.strftime("%d/%m/%Y")
	return dt_string

def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 

def send_doc(text):
	bot.send_document(app_secrets._18plus_groupid, text , caption = "Vaccine Centre Plan List\nYou can contact ANMs incase you want")
	bot.send_document(app_secrets._45plus_groupid, text , caption = "Vaccine Centre Plan List\nYou can contact ANMs incase you want")


bot.bot.send_message(app_secrets.Group_Owner , "Started...")
print("Started...")
print(dt.datetime.now().time())
num = 0
run_doc = 0
while True:
	if isNowInTimePeriod(dt.time(8,00), dt.time(22,30), dt.datetime.now().time()):
		try:
			notify.RUN()
			print(num)
			num+=1
			time.sleep(int(os.environ.get('SLEEP_TIME')))
		except Exception as e:
			if "Max retries exceeded with url:" not in str(e):
				try:
					bot.bot.send_message(app_secrets.Group_Owner , "Error!!!")
					bot.bot.send_message(app_secrets.Group_Owner , e)
				except:
					print("............\n")
					print(e , end = "\n")
			else:
				print("............\n")
				print(e , end = "\n")

			time.sleep(5)

	if isNowInTimePeriod(dt.time(14,00), dt.time(15,00), dt.datetime.now().time()):
		try:
			if run_doc == 0:
				text = centre_schedule_scrapper.scrape()
				if text[1] == current_date():
					send_doc(text[0])
					run_doc = 1
		except Exception as e:
			bot.bot.send_message(app_secrets.Group_Owner , "Error!!!")
			bot.bot.send_message(app_secrets.Group_Owner , e)

	if isNowInTimePeriod(dt.time(12,00), dt.time(13,00), dt.datetime.now().time()):
		run_doc = 0