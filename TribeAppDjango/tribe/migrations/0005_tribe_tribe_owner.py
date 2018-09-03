# Generated by Django 2.1 on 2018-09-01 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribe', '0004_tribe_tribe_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribe',
            name='tribe_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tribes', to=settings.AUTH_USER_MODEL),
        ),
    ]
