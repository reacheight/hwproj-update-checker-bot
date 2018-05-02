import telebot
import config
import scraper
import requests
import schedule
import time

bot = telebot.TeleBot(config.token)


def get_updates():
    try:
        new_accepted_count, new_unaccepted_count = scraper.task_count()
    except requests.RequestException:
        bot.send_message(config.my_id, 'request error occurred')
        return

    with open(config.data_path, 'r') as data:
        old_accepted_count, old_unaccepted_count = [int(number) for number in data.read().split()]

    with open(config.data_path, 'w') as data:
        data.write(f'{new_accepted_count} {new_unaccepted_count}')

    accepted = new_accepted_count - old_accepted_count
    unaccepted = new_unaccepted_count - old_unaccepted_count
    if accepted != 0 or unaccepted != 0:
        bot.send_message(config.my_id, f"UPDATES:\n"
                                       f"{accepted}  новых принятых задач.\n"
                                       f"{unaccepted} новых непринятых задач.")
    else:
        bot.send_message(config.my_id, "no updates")


schedule.every().hour.do(get_updates)
while True:
    schedule.run_pending()
    time.sleep(1)