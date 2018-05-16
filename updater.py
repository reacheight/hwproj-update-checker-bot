from bot import bot
import scraper
import requests
import schedule
import time
import db_manager
import logger
import config


def get_updates():
    try:
        current_accepted, current_unaccepted = [int(count) for count in db_manager.get_current_count()]
    except KeyError:
        bot.send_message(config.my_id, config.database_error_message)
        logger.add_log(config.database_error_message)
        return

    try:
        new_accepted, new_unaccepted = scraper.task_count()
    except requests.RequestException:
        bot.send_message(config.my_id, config.request_error_message)
        logger.add_log(config.request_error_message)
        return

    accepted = new_accepted - current_accepted
    unaccepted = new_unaccepted - current_unaccepted
    if accepted != 0 or unaccepted != 0:
        bot.send_message(config.my_id, f'UPDATES:\n'
                                       f'{accepted}  новых принятых задач.\n'
                                       f'{unaccepted} новых непринятых задач.')
        logger.add_log('updates')
        db_manager.set_current_count(new_accepted, new_unaccepted)
    else:
        logger.add_log('no updates')


schedule.every(config.checking_period).hours.do(get_updates)
while True:
    schedule.run_pending()
    time.sleep(1)
