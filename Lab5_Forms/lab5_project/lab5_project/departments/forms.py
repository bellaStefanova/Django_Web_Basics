from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)