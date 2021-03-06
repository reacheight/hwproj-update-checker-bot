import os

my_id = int(os.environ.get('MY_ID'))
token = os.environ.get('BOT_TOKEN')
redis_url = os.environ.get('REDIS_URL')

my_name = os.environ.get('MY_NAME')
course_url = 'http://hwproj.me/courses/31/terms/3'
logs_channel = '@hwporj_checker_logs'

accepted_db_key = 'accepted'
unaccepted_db_key = 'unaccepted'

database_error_message = 'database error occurred'
request_error_message = 'request error occurred'

checking_period = 6
