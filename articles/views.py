from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    """ A view to show users individual articles when pressed on from the main articles page """

    articles = get_object_or_404(Articles, slug=slug)

    context = {
        'articles': articles,
    }

    return render(request, 'articles/individual_article.html', context)


@login_required
def new_article(request):
    """ Gives a superuser the abilit to create new articles """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, f'Successfully created {article.title}')
            return redirect(reverse('individual_article', args=[article.slug]))
        else:
            messages.error(
                request, 'Failed to add the new article, please ensure the form is valid')
    else:
        form = ArticleForm()

    template = 'articles/new_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, slug):
    """ Gives a superuser the ability to edit an article in case of errors """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that')
        return redirect(reverse('articles'))

    article = get_object_or_404(Articles, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited the article')
            return redirect(reverse('individual_article', args=[article.slug]))
        else:
            messages.error(
                request, f'Could not edit {article.title}, please ensure the form is valid')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing "{article.title}"')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, slug):
    """ A Gives the super user the ability to delete an article """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Articles, slug=slug)
    article.delete()
    messages.success(request, f'Successfully deleted {article.title}')
    return redirect(reverse('articles'))
