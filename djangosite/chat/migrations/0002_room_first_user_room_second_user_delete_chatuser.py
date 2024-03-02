# Generated by Django 5.0.2 on 2024-02-27 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='first_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to=settings.AUTH_USER_MODEL, verbose_name='İlk Kullanıcı'),
        ),
        migrations.AddField(
            model_name='room',
            name='second_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to=settings.AUTH_USER_MODEL, verbose_name='İkinci Kullanıcı'),
        ),
        migrations.DeleteModel(
            name='ChatUser',
        ),
    ]
