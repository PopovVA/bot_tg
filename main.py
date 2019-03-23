import ptbot
import os


def reply(msg):
  # time inputed by user
  print (msg)

  # creating the common timer
  msg_tmpl = 'Timer started on {} seconds'
  msg = msg_tmpl.format(total_time)

  bot.send_message(SENDING_TO_USER_ID, msg)
  bot.create_timer(total_time, notify) 

  # creating the periodic timer
  msg_tmpl = '{}\n left {}'
  msg = msg_tmpl.format(render_progressbar(total_time,1),total_time) 
  msg_id = bot.send_message(SENDING_TO_USER_ID,msg)
  bot.create_countdown(total_time,notify_progress,msg_id=msg_id,total_time=total_time)

def notify():
  msg = "Time is over"
  bot.send_message(SENDING_TO_USER_ID, msg)

def notify_progress(secs_left,msg_id,total_time): 
  msg_tmpl = '{}\n left {}'
  msg = msg_tmpl.format(render_progressbar(total_time,total_time-secs_left),secs_left) 
  bot.update_message(SENDING_TO_USER_ID,msg_id,msg)

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

# creating the timer-bot
token = "807641815:AAEJb5P3BnF7pPGNicajReAiHHsFvPBLIs8"
SENDING_TO_USER_ID = "159421783"
bot = ptbot.Bot(token)
bot.send_message(SENDING_TO_USER_ID, "How long time timer will be working?")
bot.wait_for_msg(reply)


