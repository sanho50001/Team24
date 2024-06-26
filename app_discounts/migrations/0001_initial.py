# Generated by Django 4.2 on 2023-06-26 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_discount', models.CharField(blank=True, choices=[('percent', 'процент'), ('quantity', 'количество'), ('percent and quantity', 'процент и количество')], max_length=20, null=True, verbose_name='тип скидки')),
                ('start_discount', models.DateTimeField()),
                ('end_discount', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_discount', to='app_catalog.productinshop', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='DiscountPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(blank=True, null=True, verbose_name='процентная скидка')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='количественная скидка')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_price', to='app_discounts.discount', verbose_name='скидка')),
            ],
            options={
                'verbose_name': 'Значение скидки',
                'verbose_name_plural': 'Значения скидок',
            },
        ),
    ]
