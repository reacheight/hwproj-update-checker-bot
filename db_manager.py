import redis
import config

db = redis.from_url(config.redis_url)


def get_current_count():
    return db[config.accepted_db_key], db[config.unaccepted_db_key]


def set_current_count(new_accepted, new_unaccepted):
    db.set(config.accepted_db_key, new_accepted)
    db.set(config.unaccepted_db_key, new_unaccepted)
