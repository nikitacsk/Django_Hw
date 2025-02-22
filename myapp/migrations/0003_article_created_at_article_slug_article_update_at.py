# Generated by Django 4.2 on 2024-07-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
