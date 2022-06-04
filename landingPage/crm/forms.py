from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TimeInput(attrs={'class': 'form-control'}))
