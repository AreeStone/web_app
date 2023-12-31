# Generated by Django 4.2.4 on 2023-10-05 09:45

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('news', '0007_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
