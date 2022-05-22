from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    # formset = ArticleTagInLineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'id')
    inlines = [ArticleTagInline]
    # pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    inlines = [ArticleTagInline]
    # pass


# @admin.site.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = (ArticleTagInline,)
#     pass
#
#
# @admin.site.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     inlines = (ArticleTagInline,)
#     pass
