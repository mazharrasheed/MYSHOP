# Generated by Django 5.0 on 2024-01-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='adress',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]