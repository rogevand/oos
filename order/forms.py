from django import forms

class NameForm(forms.Form):
    post = forms.CharField(label = 'Name', max_length=100)

