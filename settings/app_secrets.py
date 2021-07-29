import os
cred = credentials.Certificate("secret")
token = os.getenv("TELEGRAM_BOT_TOKEN")
Group_Owner = os.getenv('group_owner')
Telegram_Groupid = os.getenv('telegram_groupid')
DISTRICT_CODE = os.getenv('district_code')

secret = {
  "type": os.getenv('type'),
  "project_id": os.getenv('project_id'),
  "private_key_id": os.getenv('private_key_id'),
  "private_key": os.getenv('private_key'),
  "client_email": os.getenv('client_email'),
  "client_id": os.getenv('client_id'),
  "auth_uri": os.getenv('auth_uri'),
  "token_uri": os.getenv('token_uri'),
  "auth_provider_x509_cert_url": os.getenv('as1'),
  "client_x509_cert_url": os.getenv('as2')
}