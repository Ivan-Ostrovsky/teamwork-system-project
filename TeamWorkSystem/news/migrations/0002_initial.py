# Generated by Django 5.0.3 on 2024-06-09 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='corporationnews',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='News', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newscomments',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='news.corporationnews'),
        ),
        migrations.AddField(
            model_name='newscomments',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
