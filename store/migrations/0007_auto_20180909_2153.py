# Generated by Django 2.1 on 2018-09-10 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
    ]
