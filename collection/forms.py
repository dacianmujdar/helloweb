from django.forms import ModelForm

from collection.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'description')
