# Generated by Django 3.2.5 on 2022-09-26 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_det',
            name='Active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product_det',
            name='currency_type',
            field=models.CharField(default='INR', max_length=10),
        ),
        migrations.CreateModel(
            name='tag_pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_products', models.TextField(max_length=500)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.product_det')),
            ],
            options={
                'db_table': 'tag_product',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.product_det')),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]