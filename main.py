import notify
from settings import app_secrets
import time
import datetime as dt
import os

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
	if isNowInTimePeriod(dt.time(9,00), dt.time(22,30), dt.datetime.now().time()):
		try:
			notify.RUN()
			print(num)
			num+=1
			time.sleep(int(os.environ.get('time')))
		except Exception as e:
			if "Max retries exceeded with url:" not in str(e):
				try:
					exception_type, exception_object, exception_traceback = sys.exc_info()
					filename = exception_traceback.tb_frame.f_code.co_filename
					line_number = exception_traceback.tb_lineno
					e = e + "\n"+"\n"+"Exception type: "+exception_type+"\n"+"File name: "+filename+"\n"+"Line number: "+line_number
					notify.bot.send_message(app_secrets.Group_Owner , "Error!!!")
					notify.bot.send_message(app_secrets.Group_Owner , e)
				except:
					print("............\n")
					print(e , end = "\n")
			else:
				print("............\n")
				print(e , end = "\n")

			time.sleep(5)

