import telebot
import firebase_admin
from firebase_admin import credentials , firestore
from telebot import types
from settings import app_secrets

# /////////////////////////////////////////////////////

# initializing firestore database for under45 group
cred_under45 = credentials.Certificate(app_secrets.secret_under_45)
under45 = firebase_admin.initialize_app(cred_under45,name="Under45KanpurNagar")
db_under45 = firestore.client(under45)

# initializing firestore database for above45 group
cred_above45 = credentials.Certificate(app_secrets.secret_above_45)
above45 = firebase_admin.initialize_app(cred_above45,name="Above45KanpurNagar")
db_above45 = firestore.client(above45)

# initializing bot which will send messages to the groups
bot = telebot.TeleBot(token = app_secrets.token)

# /////////////////////////////////////////////////////
 
# BUTTONS.........................

# markup button which will appear bellow every message that will be sent to the group on clicking this u will be redirected to the cowin's official site for booking your slots
markup = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton('BOOK NOW', url = "https://selfregistration.cowin.gov.in/")
markup.add(btn)

# ///////////////////////////////////////////////////////////////////////////////////////////////////

