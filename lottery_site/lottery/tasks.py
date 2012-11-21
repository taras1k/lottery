from celery import task
from lottery.operations import Lottery
from facepy import GraphAPI

@task()
def add(x, y):
    lottery = Lottery()
    lottery.data['page_id'] = 0
    lottery.save()
    return x + y

@task()
def check_lotteries():
    lottery = Lottry()
    for incompleted_lotteries in lottery.get_incompleted():
        graph = GraphAPI(incompleted_lotteries['token'])
        page = graph.get(incompleted_lotteries['page_id'])
        if page.get('likes', 0) >= incompleated_lotteries['']
        pass
