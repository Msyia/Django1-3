from django import forms
from .models import Customer  # Pastikan menggunakan .models untuk mengimpor Customer

class NewSubscriber(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
