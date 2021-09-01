from twilio.rest import Client
from SMS.setting import ACCOUNT_SID
from SMS.setting import AUTH_TOKEN
from SMS.setting import MY_PHONE_NUMBER

# 建立 client instance
client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages \
                .create(
                    from_="+13367777181",
                    to=MY_PHONE_NUMBER,
                    body="唷西西超可愛唷，柏柔柔也超可愛唷，只有阿牛牛最欠揍唷。",
                 )

print(message.sid)
