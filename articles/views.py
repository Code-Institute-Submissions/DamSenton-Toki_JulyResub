from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Articles

from .forms import ArticleForm


# Create your views here.


def articles(request):
    """ A view to return the articles page """

    articles = Articles.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, 'articles/articles.html', context)


def individual_article(request, slug):
    """ A view to return individual blog post page """

    articles = get_object_or_404(Articles, slug=slug)

    context = {
        'articles': articles,
    }

    return render(request, 'articles/individual_article.html', context)
