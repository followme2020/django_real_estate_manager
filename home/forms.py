from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=20, label='First name', widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    lastname = forms.CharField(max_length=20, label='Last name', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(required=False, label='Your email address', widget=forms.EmailInput(attrs={'placeholder': 'example@corporate.com', 'style': 'width: 300px;', 'class': 'form-control'}))
    phonenum = forms.CharField(label='Your phone number', required=True, widget=forms.NumberInput(attrs={'placeholder': '050-5552255', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message', 'style': 'width: 300px;', 'class': 'form-control'}))
