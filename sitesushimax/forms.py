from .models import Order, Cart
from django import forms


class OrderingForm(forms.ModelForm):
    """Форма создания заказа"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ['user_name', 'phone', 'address', 'payment']

