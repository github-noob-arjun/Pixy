from os import environ
from logging import basicConfig, INFO, StreamHandler, getLogger, WARNING, Logger
from logging.handlers import RotatingFileHandler
from script import StartTxT, HelpTxT, AboutTxT

basicConfig( level=INFO, format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S', handlers=[ RotatingFileHandler("filtersbot.txt", maxBytes=50000000, backupCount=10), StreamHandler() ] )

getLogger("pyrogram").setLevel(WARNING)

def LOGGER(name: str) -> Logger:
    return getLogger(name)

API_ID = 15681435
API_HASH = "29021e7d8f6fe5338a45470115567f9e"
BOT_TOKEN = "5931770179:AAEqas4UAjqSeK_w849pFvAdv92YSVeejPo"
PORT = 8080
