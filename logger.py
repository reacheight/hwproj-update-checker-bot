from bot import bot
import config


def add_log(message):
    bot.send_message(config.logs_channel, message)