from django import forms
from lottery.operations import Lottery

class StartForm(forms.Form):
    name = forms.CharField()

class PageForm(forms.Form):
    name = forms.CharField()

class LotteryForm(forms.Form):
    name = forms.CharField(initial='name o lottery')
    likes_to_finish = forms.IntegerField()

    def save_lottery(self, page_id, token):
        #save lottery using the self.cleaned_data dictionary
        lottery = Lottery()
        lottery.data['page_id'] = page_id
        lottery.data['completed'] = 0
        lottery.data['token'] = token
        lottery.data = self.cleaned_data
        lottery.save()
