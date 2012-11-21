from django import forms
from lottery.operations import Lottery

class StartForm(forms.Form):
    name = forms.CharField()

class PageForm(forms.Form):
    name = forms.CharField()

class LotteryForm(forms.Form):
    name = forms.CharField(initial='name o lottery')
    image = forms.ImageField()
    likes_to_finish = forms.IntegerField()

    def save_lottery(self, page_id, token):
        #save lottery using the self.cleaned_data dictionary
        data = self.cleaned_data
        data['page_id'] = page_id
        data['token'] = token
        lottery = Lottery(data)
        lottery.start()
