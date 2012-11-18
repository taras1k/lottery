from lottery_site.settings import db


class BaseModel(object):

    def __init__(self, collection_name):
        self.data = {}
        self.collection = db['lottery']

    def save(self):
        self.collection.save(self.data)

    def query_one(self, query):
        queried_object = self.collection.find_one(query)
        if queried_object:
            return queried_object
        return {}

    def query_many(self, query):
        return self.collection.find(query)

    def get_by_id(self, id):
        query = {'id': id}
        self.data = self.query_one(query)
        return self.data

class LotteryModel(BaseModel):

    def __init__(self):
        super(LotteryModel, self).__init__('lottery')
