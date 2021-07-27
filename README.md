# Cowin_Slots_notifier_TelegramBot
This Telegram bot looks for available slots in the preferred district and send you a message on configured Telegram group.
Running on an Indian Server is must.<br/>
<br/>
**Update app_secrets.py and secrets.json file**<br/>
```javascript
{
  "type": "TYPE_OF_ACCOUNT",
  "project_id": "PROJECT_NAME",
  "private_key_id": "PRIVATE_ID",
  "private_key": "PRIVATE_KEY",
  "client_email": "FIREBASE_CLIENT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "AUTH",
  "token_uri": "TOKEN",
  "auth_provider_x509_cert_url": "AUTH_PROVIDER",
  "client_x509_cert_url": "CLIENT_URL"
}

cred = credentials.Certificate("secrets.json")
token = "TELEGRAM_BOT_TOKEN"
Group_Owner = "ID_OF_OWNER"
Telegram_Groupid = "TELEGRAM_GROUP_ID"
DISTRICT_CODE = "CODE_OF YOUR DISTRICT"
```
**Get State Code**
```javascript
https://cdn-api.co-vin.in/api/v2/admin/location/states
```
<br/>

**Get District Code**
```javascript
https://cdn-api.co-vin.in/api/v2/admin/location/districts/{State_id}
```
<br/>

**RUN**
```javascript
python main.py
```
