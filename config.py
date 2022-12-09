#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfathera
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5955102343:AAFSCecMMctLH5M5Qsu8Qh9eCqaglua3v2s")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6216349"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001866386001"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5158607797"))

#Port
PORT = os.environ.get("PORT", "3356")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://asubang:asubang@cluster0.gbyc7wo.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "telemsu")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001820597151"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nSaya Dapat Menyimpan File Pribadi Dan Pengguna Lain Dapat Mengaksesnya Dari Tautan Khusus.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5158607797 1850233338 5545756173").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Anda harus bergabung di Channel/Group Untuk Menggunakan Saya\n\nSilakan Bergabung Terlebih Dahulu</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Jangan Kirimi Saya Pesan Secara Langsung. Saya Hanya Bisa Digunakan Admin channel!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
