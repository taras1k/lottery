from lottery.models import LotteryModel
from facepy import GraphAPI

class BaseOperations(object):

    def __init__(self, model):
        self.model = model()

    def save(self):
        self.model.data = self.data
        self.model.save()

class Lottery(BaseOperations):

    def __init__(self, data={}):
        self.data = data
        super(Lottery, self).__init__(LotteryModel)

    def get_incompleted(self):
        query = {'completed': 0}
        return self.model.query_many(query)

    def start(self):
        self.data['completed'] = 0
        graph = GraphAPI(self.data['token'])
        page_token = ''
        for account in graph.get('me/accounts', page=True):
            for page in account['data']:
                if page['id'] == self.data['page_id']:
                    page_token = page['access_token']
                    break
            if page_token:
                break
        if page_token and 'image' in self.data:
            graph = GraphAPI(page_token)
            graph.post('%s/feed' % self.data['page_id'],
                image=self.data['image'].read())
            del self.data['image']
        self.save()

