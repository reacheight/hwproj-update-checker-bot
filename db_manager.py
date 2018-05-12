import redis
import config

db = redis.from_url(config.redis_url)


def get_current_count():
    return db.get('accepted'), db.get('unaccepted')


def set_current_count(new_accepted, new_unaccepted):
    db.set('accepted', new_accepted)
    db.set('unaccepted', new_unaccepted)
