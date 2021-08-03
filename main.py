import notify
from settings import app_secrets
import time
import datetime as dt

def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 



notify.bot.send_message(app_secrets.Group_Owner , "Started...")
print("Started...")
print(dt.datetime.now().time())
num = 0
while True:
	if isNowInTimePeriod(dt.time(22,30), dt.time(11,30), dt.datetime.now().time()):
		try:
			notify.RUN()
			print(num)
			num+=1
			time.sleep(50)
		except Exception as e:
			if "Max retries exceeded with url:" not in str(e):
				try:
					notify.bot.send_message(app_secrets.Group_Owner , "Error!!!")
					notify.bot.send_message(app_secrets.Group_Owner , e)
				except:
					print("............\n")
					print(e , end = "\n")
			else:
				print("............\n")
				print(e , end = "\n")

			time.sleep(5)

