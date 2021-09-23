
# # ex --- [[id,age],[id,age]]
# Personal_Config = json.loads(os.environ.get('PERSONAL_CONFIG'))

# #[dd/mm/yyyy,dd/mm/yyyy]
# PERSONAL_SEND_DATE = json.loads(os.environ.get('PERSONAL_DATES'))

# PERSONAL_SEND_VACCINE = "/COVAXIN/COVISHIELD/SPUTNIK V/"

# # True or False
PERSONAL_RUN = False

# ///////////////////////////////////////////////////////////////////////////////////////////////////

def personal_notify(vaccine , date , text , age):
	print("Currently Not Working")
	# for i in Personal_Config:
	# 	if vaccine == PERSONAL_SEND_VACCINE and date in PERSONAL_SEND_DATE :
	# 		for user in i:
	# 			if age == user[1]:
	# 				bot.bot.send_message( user[0] , text ,parse_mode ="Markdown",reply_markup = bot.markup)

# /////////////////////////////////////////////////////
