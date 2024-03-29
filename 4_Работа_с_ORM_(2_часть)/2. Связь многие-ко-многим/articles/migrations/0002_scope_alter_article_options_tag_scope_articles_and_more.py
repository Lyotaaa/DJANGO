# Generated by Django 4.2.1 on 2023-06-07 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scope",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_main", models.BooleanField(verbose_name="Основная метка")),
            ],
        ),
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["-published_at"],
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=30, verbose_name="Метка")),
                (
                    "article",
                    models.ManyToManyField(
                        related_name="articles",
                        through="articles.Scope",
                        to="articles.article",
                        verbose_name="Статьи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Метка",
                "verbose_name_plural": "Метки",
            },
        ),
        migrations.AddField(
            model_name="scope",
            name="articles",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
                verbose_name="Метка",
            ),
        ),
        migrations.AddField(
            model_name="scope",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
                verbose_name="Метка",
            ),
        ),
    ]
