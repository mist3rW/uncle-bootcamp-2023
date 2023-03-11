from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject','email','sender', 'detail')
        widgets = {
           'subject': forms.TextInput(attrs={
               'class': 'form-control col-xl-8'
           }),
           'email': forms.EmailInput(attrs={
               'class': 'form-control col-xl-8'
           }),
           'sender': forms.TextInput(attrs={
               'class': 'form-control col-xl-8'
           }),
           'detail': forms.Textarea(attrs={
               'class': 'form-control col-xl-8'
           })
       }