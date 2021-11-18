# Generated by Django 4.0b1 on 2021-11-18 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('enterprise', models.CharField(max_length=50)),
                ('customer', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('pay_way', models.CharField(choices=[('cash', '현금'), ('credit', '카드')], max_length=10, verbose_name='pay_way')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('memo', models.TextField(blank=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='enterprise.enterprise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
