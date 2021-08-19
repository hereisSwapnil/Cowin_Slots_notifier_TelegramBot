import os

secret = {
  "type": os.environ.get('type'),
  "project_id": os.environ.get('project_id'),
  "private_key_id": os.environ.get('private_key_id'),
  "private_key": os.environ.get('private_key').replace('\\n', '\n'),
  "client_email": os.environ.get('client_email'),
  "client_id": os.environ.get('client_id'),
  "auth_uri": os.environ.get('auth_uri'),
  "token_uri": os.environ.get('token_uri'),
  "auth_provider_x509_cert_url": os.environ.get('as1'),
  "client_x509_cert_url": os.environ.get('as2')
}


token = os.environ.get("TELEGRAM_BOT_TOKEN")
Group_Owner = os.environ.get('group_owner')
_18plus_groupid = os.environ.get('telegram_groupid_18')
_45plus_groupid = ('telegram_groupid_45')
DISTRICT_CODE = os.environ.get('district_code')

