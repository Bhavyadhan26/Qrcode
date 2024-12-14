# Generated by Django 5.0.2 on 2024-12-14 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem')),
            ],
        ),
    ]