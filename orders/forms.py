
from django import forms
from django_countries.widgets import CountrySelectWidget
from orders.models import Orders


class PaymentProcessForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'country', 'city', 'street_name', 'house_number','postal_code',
                  'credit_card_number', 'credit_card_holder', 'credit_card_expiry_month', 'credit_card_expiry_year', 'cvc')

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'country', 'city', 'street_name', 'house_number', 'postal_code')
        widgets = {
            'first_name': forms.widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'last_name': forms.widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'country': CountrySelectWidget(),
            'city': forms.widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'street_name': forms.widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'house_number': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'postal_code': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '10'})
        }

class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('credit_card_number', 'credit_card_holder', 'credit_card_expiry_month', 'credit_card_expiry_year', 'cvc')
        widgets = {
            'credit_card_number': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '16'}),
            'credit_card_holder': forms.widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'credit_card_expiry_month': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'credit_card_expiry_year': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'cvc': forms.widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '3'})
        }

