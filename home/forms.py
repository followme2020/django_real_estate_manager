from django import forms
from collections import OrderedDict
from home.models import LeadUser


class ContactForm(forms.ModelForm):
    class Meta:
        model = LeadUser
        fields = {'firstname', 'lastname', 'email', 'phone_number', 'message'}
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last name', 'style': 'width: 300px;', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@corporate.com', 'style': 'width: 300px;', 'class': 'form-control'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': '+972505552255', 'style': 'width: 300px;', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message', 'style': 'width: 300px;', 'class': 'form-control'}),
        }



    def save(self, commit=True):
        lead = super().save(commit=False)
        if commit:
            lead.save()
        return lead


ContactForm.base_fields = OrderedDict(
            (k, ContactForm.base_fields[k])
            for k in ['firstname', 'lastname', 'email', 'phone_number', 'message']
        )
