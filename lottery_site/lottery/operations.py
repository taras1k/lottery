from lottery.models import LotteryModel

class BaseOperations(object):

    def __init__(self, model):
        self.model = model()

    def save(self):
        self.model.data = self.data
        self.model.save()

class Lottery(BaseOperations):

    def __init__(self):
        self.data= {}
        super(Lottery, self).__init__(LotteryModel)

    def get_incompleted(self):
        query = {'completed': 0}
        return self.model.query_many(query)
