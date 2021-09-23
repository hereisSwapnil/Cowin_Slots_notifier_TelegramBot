#It will be used for reading secret vars from the os
import os
import json

#This is the auth secret json key for firestore 
#You can get it from firebase settings

# fireauths for under 45 group
secret_under_45 = json.loads(os.environ.get('FIREBASE_UNDER_45'))

# fireauths for above 45 group
secret_above_45 = json.loads(os.environ.get('FIREBASE_ABOVE_45'))


#Token of telegram bot got from bot father
token = str(os.environ.get('BOT_TOKEN'))
#Username of the owner/manager who will recieve message if any issue occurred in the bot
Group_Owner = int(os.environ.get('GROUP_OWNER_ID'))
#Group ID of 18 Plus group
_18plus_groupid = int(os.environ.get('18PLUS_GROUP_ID'))
#Group ID of 45 Plus group
_45plus_groupid = int(os.environ.get('45PLUS_GROUP_ID'))
#District code as in cowin api
#You can find District code from the https://apisetu.gov.in/
DISTRICT_CODE = int(os.environ.get('DISTRICT_CODE'))

