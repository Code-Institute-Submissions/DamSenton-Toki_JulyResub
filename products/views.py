from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm

# Create your views here.


def all_products(request):
    """ A view to show all products, includes sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(
                    request, "You did not enter anys earch criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product_review_form = ProductReviewForm()
    reviews = ProductReview.objects.filter(
        product_id=product_id).order_by('-date_created')

    context = {
        'product': product,
        'product_review_form': product_review_form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Add product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'You have succesfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, f'Failed to edit {product.name}, please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product form the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(
        request, f'Successfully deleted {product.name} from the store!')
    return redirect(reverse('products'))


def new_product_review(request, product_id):
    """
    A view to allow customers to rate
    a product if they are logged in
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_review_form = ProductReviewForm(request.POST)
        if product_review_form.is_valid():
            review = product_review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(
                request, f'Thank you for leaving a review for {product.name}')
            return redirect(reverse('product_detail', args=[product_id]))
    print(product_review_form)
    return redirect(reverse('product_detail', args=[product_id]))
