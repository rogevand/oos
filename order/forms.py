from django import forms

class NameForm(forms.Form):
    post = forms.CharField(label = 'Name', max_length=100)

class ServiceForm(forms.Form):

    date  = forms.CharField(label='date', max_length=100)
    leader = forms.CharField(label='leader', max_length=100)
    theme=  forms.CharField(label='theme', max_length=100)
    prelude_time = forms.CharField(label='prelude_time', max_length=100)
    sermon= forms.CharField(label='sermon', max_length=100)
    announcements = forms.CharField(label='announcements', max_length=100)
    musician1 = forms.CharField(label='musician1', max_length=100)
    musician2 = forms.CharField(label='musician2', max_length=100)