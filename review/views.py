from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from .forms import Product_review_form


def review_form_page(request, product_id):
    """ A view to take a user to the review form """
    return render(request, 'review/review-form.html')


def new_review(request, product_id):
    """
    Handles the POST request for review form. Saves the form and redirects
    to the product selected page
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = Product_review_form(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.info(
                request, "Thank you for the review!")
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            print(review_form.errors)

    return redirect(reverse('product_detail', args=[product_id]))
