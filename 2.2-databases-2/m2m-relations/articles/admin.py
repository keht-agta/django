from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class TaginlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        articles_count = 0
        for form in self.forms:
            data = form.cleaned_data
            if data and not data.get('DELETE', ''):
                articles_count += 1
            if data.get('is_main', '') and not data.get('DELETE',''):
                is_main_count += 1

        # print(articles_count, is_main_count)
        # если общее кол-во 0 или главных !=1 после сохранения с учетом удаления, то ошибка
        if articles_count == 0 or is_main_count != 1:
            raise ValidationError('Кол-во общих и главных тэгов неверно. Общее кол-во > 0, главных = 1 ')
        return super().clean()  # вызываем базовый код переопределяемого метода

class TagInline(admin.TabularInline):
    model = Scope
    formset = TaginlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline,]

@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    # list_display = ['id', 'scope']
