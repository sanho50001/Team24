# Generated by Django 4.2 on 2023-07-10 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0003_alter_comments_options_alter_productinshop_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='buying_type',
            new_name='delivery',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('not paid', 'Не оплачен'), ('paid for', 'Оплачен')], default='not paid', max_length=25, verbose_name='Статус заказа'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Цена товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_orders.order', verbose_name='Заказ')),
                ('product_in_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_catalog.productinshop', verbose_name='Товар')),
            ],
        ),
    ]