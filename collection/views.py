from django.shortcuts import render
from collection.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles,
    })
