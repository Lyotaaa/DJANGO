# Generated by Django 4.2.1 on 2023-06-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_scope_alter_article_options_tag_scope_articles_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="tag_name",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="scope",
            name="articles",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
                verbose_name="Метки",
            ),
        ),
        migrations.AlterField(
            model_name="scope",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
                verbose_name="Метки",
            ),
        ),
    ]
