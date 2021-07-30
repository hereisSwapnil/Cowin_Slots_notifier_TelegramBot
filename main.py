import notify
from settings import app_secrets
import time

notify.bot.send_message(app_secrets.Group_Owner , "Started...")
print("Started...")

while True:
	try:
		notify.RUN()
		time.sleep(20)
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