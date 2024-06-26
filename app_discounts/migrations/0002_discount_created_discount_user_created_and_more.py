# Generated by Django 4.2 on 2023-07-04 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_discounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания скидки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='user_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь создавший скидку'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='type_discount',
            field=models.CharField(blank=True, choices=[('процент', 'процент'), ('количество', 'количество'), ('процент и количество', 'процент и количество')], max_length=20, null=True, verbose_name='тип скидки'),
        ),
    ]
