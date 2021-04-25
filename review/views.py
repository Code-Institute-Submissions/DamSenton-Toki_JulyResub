from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


# Create your views here.


def new_review(request, product_id):
    """
    A view to take users to a review page where
    they can leave a message and a rating for a product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'review/review_form.html', context)
