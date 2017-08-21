from django.contrib import admin
from collection.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('name', 'description', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Article, ArticleAdmin)
