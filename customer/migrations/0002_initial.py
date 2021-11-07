# Generated by Django 4.0b1 on 2021-11-07 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_groups', to='enterprise.enterprise'),
        ),
        migrations.AddField(
            model_name='customer',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='enterprise.enterprise'),
        ),
        migrations.AddField(
            model_name='customer',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='customer.group'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('enterprise', 'name')},
        ),
    ]
