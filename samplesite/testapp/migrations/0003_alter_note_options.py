# Generated by Django 4.2 on 2023-09-27 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'permissions': (('hide_comments', 'Можно скрывать заметки'),)},
        ),
    ]
