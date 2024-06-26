from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "phone_number",
            "email",
            "city",
            "address",
            "delivery",
            "payment",
            "comment",
            "status",
        )
