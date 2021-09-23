import bot
from settings import app_secrets
import time
import datetime as dt
import os
import notify

def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 



bot.bot.send_message(app_secrets.Group_Owner , "Started...")
print("Started...")
print(dt.datetime.now().time())
num = 0
while True:
	if isNowInTimePeriod(dt.time(9,00), dt.time(22,30), dt.datetime.now().time()):
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

