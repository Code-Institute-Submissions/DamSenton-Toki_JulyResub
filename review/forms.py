from django import forms
from django.forms import Textarea
from .models import Product_review


class Product_review_form(forms.ModelForm):

    class Meta:
        model = Product_review
        widgets = {
            'review': Textarea(attrs={'cols': 7, 'rows': 7}),
        }
        fields = ['subject', 'review', 'rating']
        labels = {
            'rating': 'Select a rating'
        }
