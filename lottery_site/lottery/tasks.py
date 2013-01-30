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
    lotteries = Lottery()
    for lottery in lotteries.get_incompleted():
        graph = GraphAPI(lottery['page_token'])
        page = graph.get(lottery['post_id'])
        if page.get('likes', 0) >=lottery['likes_to_finish']:
            fb_page = GraphAPI(lottery['page_token'])
            post = graph.post(path='%s/feed' % lottery['page_id'],
                message='success')
        post = graph.post(path='%s/feed' % lottery['page_id'],
            message='test cel')
