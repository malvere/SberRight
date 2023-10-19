# ENV impots
import os
import socket

HOST = socket.gethostname()
if HOST.endswith(".local"):
    print(f"Running on local machine ({HOST})")
    from dotenv import load_dotenv
    WEBHOOK_HOST = "localhost"
    load_dotenv("bot/py.env")
    PORT = 8000
else:
    print(f"Running on non-local machine ({HOST})")
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    WEBHOOK_HOST = f"https://{PROJECT_NAME}.onrender.com" # Enter here your link from project settings

""" !Add PROJECT_NAME in  enVars! """

""" Webhook """
API_TOKEN = str(os.getenv("API_TOKEN"))

  
WEBHOOK_URL_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = os.getenv("localhost")
WEBAPP_PORT = os.getenv("PORT")

""" Administration and Restrictions """
SERVICE_CHANNEL_ID = os.getenv("SERVICE_CHANNEL_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Channel Id (bot should be added to it with admin priveleges)
CHANNEL_URL = os.getenv("CHANNEL_URL")  # Channel url to output for non-member users

# Filters CallBackCalls to be added to member-only list (see handlers.callback.tools for more info)
CALL_FILTERS = str(os.getenv("CALL_FILTERS")).split("\/")
ADMIN = os.getenv("ADMIN")  # Get user which will have access for admin priveleges


""" Timers in Minutes"""


SCHEDULE_TIMER = float(os.getenv("SCHEDULE_TIMER", 60))
NEXT_POST_TIMER = SCHEDULE_TIMER * 2
REMINDER_TIMER = float(os.getenv("REMINDER_TIMER", 15))
FAQ_AWAIT = 0.5
ARTICLE_TIMER = float(os.getenv("ARTICLE_TIMER", 3))
DATA_8_TIMER = int(os.getenv("DATA_8_TIMER", 15))


""" DataBase """

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
