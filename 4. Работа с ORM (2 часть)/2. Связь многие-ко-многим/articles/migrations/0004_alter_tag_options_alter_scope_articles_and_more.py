# Generated by Django 4.2.1 on 2023-06-10 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_rename_tag_name_tag_name_alter_scope_articles_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Раздел", "verbose_name_plural": "Разделы"},
        ),
        migrations.AlterField(
            model_name="scope",
            name="articles",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
                verbose_name="Разделы",
            ),
        ),
        migrations.AlterField(
            model_name="scope",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
                verbose_name="Разделы",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Раздел"),
        ),
    ]
