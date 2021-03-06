from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'title',
            'price',
            'isDiscounted',
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "titleDesign"}),
        }
