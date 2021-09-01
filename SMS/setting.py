import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
ACCOUNT_SID = os.getenv("ACCOUNT_SID")  # 通常固定不變之參數以全大寫命名
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
