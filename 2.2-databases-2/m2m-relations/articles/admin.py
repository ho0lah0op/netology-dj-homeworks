from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            flag = form.cleaned_data.get('is_main')
            counter += 1 if flag else 0

        if counter > 1:
            raise ValidationError('Ошибка: Основной тег только один')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
