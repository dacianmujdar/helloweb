from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from collection.forms import ArticleForm
from collection.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles,
    })


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required
def edit_article(request, slug):
    article = Article.objects.get(slug=slug)
    if article.owner != request.user:
        raise Http404
    form_class = ArticleForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = form_class(instance=article)
    return render(request, 'articles/edit_article.html', {
        'article': article,
        'form': form
    })


def create_article(request):
    form_class = ArticleForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.name)
            article.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = form_class()

    return render(request, 'articles/create_article.html', {
        'form': form,
    })


def browse_by_name(request, initial=None):
    if initial:
        articles = Article.objects.filter(
             name__istartswith=initial).order_by('name')
    else:
        articles = Article.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'articles': articles,
        'initial': initial,
    })
