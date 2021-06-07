# Cowin_Slots_notifier_TelegramBot
This Telegram bot looks for available slots in the preferred district and send you a message on configured Telegram group.<br/>
<br/>
**Update config.py and secrets.json file**<br/>
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

cred = credentials.Certificate("PATH_TO_FIRESTORE_CREDENTIALS")
token = "TELEGRAM_BOT_TOKEN"
id1 = ID_OF_OWNER
qq = TELEGRAM_GROUP_ID
```
**RUN**
```javascript
python notify.py
```
