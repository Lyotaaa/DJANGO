from django.contrib import admin
from articles.models import Article, Tag, Scope
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main") == True:
                count += 1
            if count > 1:
                raise ValidationError("Эсновной может быть только один раздел")
            elif count == 0:
                raise ValidationError("Укажите основной раздел")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
