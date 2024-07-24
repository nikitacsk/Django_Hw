# Generated by Django 4.2 on 2024-07-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_article_created_at_article_slug_article_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'catalog',
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
