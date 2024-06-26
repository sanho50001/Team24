# Generated by Django 4.2 on 2023-07-04 06:30

import app_users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_discounts', '0005_alter_discount_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='user_created',
            field=models.ForeignKey(auto_created=app_users.models.User, blank=app_users.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь создавший скидку'),
        ),
    ]
