from django.shortcuts import render
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
