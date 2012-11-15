from django import forms

class StartForm(forms.Form):
    name = forms.CharField()

class PageForm(forms.Form):
    name = forms.CharField()

class LotteryForm(forms.Form):
    name = forms.CharField(initial='name o lottery')
    likes_to_finish = forms.DecimalField()

    def save_lottery(self):
        #save lottery using the self.cleaned_data dictionary
        pass
