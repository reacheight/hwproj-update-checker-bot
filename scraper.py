import config
import requests
from bs4 import BeautifulSoup


def task_count():
    accepted_count = 0
    unaccepted_count = 0

    response = requests.get(config.url)
    response.raise_for_status()
    page = BeautifulSoup(response.content, 'html5lib')

    table = page.find('table', {'class': 'table table-bordered table-condensed'}).find_all('tr')
    for tr_tag in table:
        if config.my_name in tr_tag.get_text():
            for tag in tr_tag.find_all('td', {'style': 'padding: 0'}):
                task = tag['class']
                if len(task) > 1:
                    if task[1] == 'accepted-task':
                        accepted_count += 1
                    elif task[1] == 'task-with-notes':
                        unaccepted_count += 1

    return accepted_count, unaccepted_count
