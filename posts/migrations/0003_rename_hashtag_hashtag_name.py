# Generated by Django 4.0.6 on 2022-08-03 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_category_name_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag',
            new_name='name',
        ),
    ]
