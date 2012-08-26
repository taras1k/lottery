from django import forms

class StartForm(forms.Form):
    name = forms.CharField()

