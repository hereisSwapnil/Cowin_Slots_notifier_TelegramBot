import os

secret = {
  "type": os.environ('type'),
  "project_id": os.environ('project_id'),
  "private_key_id": os.environ('private_key_id'),
  "private_key": os.environ('private_key'),
  "client_email": os.environ('client_email'),
  "client_id": os.environ('client_id'),
  "auth_uri": os.environ('auth_uri'),
  "token_uri": os.environ('token_uri'),
  "auth_provider_x509_cert_url": os.environ('as1'),
  "client_x509_cert_url": os.environ('as2')
}


token = os.environ("TELEGRAM_BOT_TOKEN")
Group_Owner = os.environ('group_owner')
Telegram_Groupid = os.environ('telegram_groupid')
DISTRICT_CODE = os.environ('district_code')

