import telebot
import scraper
import requests
import schedule
import time
import config

current_accepted = 0
current_unaccepted = 0

bot = telebot.TeleBot(config.token)


def get_updates():
    global current_accepted, current_unaccepted

    try:
        new_accepted, new_unaccepted = scraper.task_count()
    except requests.RequestException:
        bot.send_message(config.my_id, 'request error occurred')
        return

    accepted = new_accepted - current_accepted
    unaccepted = new_unaccepted - current_unaccepted
    if accepted != 0 or unaccepted != 0:
        bot.send_message(config.my_id, f"UPDATES:\n"
                                       f"{accepted}  новых принятых задач.\n"
                                       f"{unaccepted} новых непринятых задач.")

    current_accepted, current_unaccepted = new_accepted, new_unaccepted


schedule.every(2).hours.do(get_updates)
while True:
    schedule.run_pending()
    time.sleep(1)