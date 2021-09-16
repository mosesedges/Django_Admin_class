from django.forms import ModelForm
from .models import FirstCustomer


class CustomerForm(ModelForm):
    class Meta:
        model = FirstCustomer
        fields = '__all__'
