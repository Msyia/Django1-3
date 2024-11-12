from django import forms
from django.core import validators

# def check_for_a(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError('Name should start with A')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Input your email again:')
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        
        if email != v_email:
            raise forms.ValidationError('Emails do not match')
