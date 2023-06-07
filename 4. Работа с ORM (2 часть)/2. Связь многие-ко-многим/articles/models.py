from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-published_at"]
        
    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=30, verbose_name="Метка")
    article = models.ManyToManyField(Article, through="Scope", related_name="articles", verbose_name="Статьи")

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Метки"

    def __str__(self) -> str:
        return self.tag_name
class Scope(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="scopes", verbose_name="Метка")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="scopes", verbose_name="Метка")
    is_main = models.BooleanField(verbose_name="Основная метка")