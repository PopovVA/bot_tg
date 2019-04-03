import telepot
from telepot.loop import MessageLoop
import time
import requests


SetProxy = telepot.api.set_proxy("https://45.250.178.36:8080")
bot = telepot.Bot('807641815:AAEJb5P3BnF7pPGNicajReAiHHsFvPBLIs8')

def send_message(msg):
  url = 'http://mvadimpopov.pythonanywhere.com/msg_from_bot'
  name = msg["from"]["first_name"]
  telegram_id = msg["from"]["id"]
  text = msg["text"]  
  data = {"name":name,"telegram_id":str(telegram_id),"text":text}
  response = requests.post(url,data=data)

def handle(msg):
  send_message(msg)

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
