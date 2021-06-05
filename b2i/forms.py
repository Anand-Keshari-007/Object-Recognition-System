from django import forms


class predictForm(forms.Form):
    choose_image = forms.ImageField()
