#It will be used for reading secret vars from the os
import os

#This is the auth secret json key for firestore 
#You can get it from firebase settings

# fireauths for under 45 group
secret_under_45 = {
  "type": "service_account",
  "project_id": os.environ.get('UNDER45_PROJECT_ID'),
  "private_key": os.environ.get('PRIVATE_KEY_UNDER45').replace('\\n', '\n'),
  "client_email": os.environ.get('CLIENT_EMAIL_UNDER45'),
  "client_id": os.environ.get('U1'),
  "auth_uri": os.environ.get('U2'),
  "token_uri": os.environ.get('U3'),
  "auth_provider_x509_cert_url": os.environ.get('U4'),
  "client_x509_cert_url": os.environ.get('U5')
}

# fireauths for above 45 group
secret_above_45 = {
  "type": "service_account",
  "project_id": os.environ.get('ABOVE45_PROJECT_ID'),
  "private_key": os.environ.get('PRIVATE_KEY_ABOVE45').replace('\\n', '\n'),
  "client_email": os.environ.get('CLIENT_EMAIL_ABOVE45'),
  "client_id": os.environ.get('A1'),
  "auth_uri": os.environ.get('A2'),
  "token_uri": os.environ.get('A3'),
  "auth_provider_x509_cert_url": os.environ.get('A4'),
  "client_x509_cert_url": os.environ.get('A5')
}


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

