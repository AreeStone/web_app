# Generated by Django 4.2.4 on 2023-10-02 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articles_borrower_alter_articles_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='borrower',
            new_name='author',
        ),
    ]
