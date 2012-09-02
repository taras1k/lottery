from django import forms

class StartForm(forms.Form):
    name = forms.CharField()


class PageForm(forms.Form):
    name = forms.CharField()

