# Generated by Django 5.0.3 on 2024-06-10 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newscomments',
            old_name='writer',
            new_name='author',
        ),
    ]
