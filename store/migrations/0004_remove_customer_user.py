# Generated by Django 4.1.5 on 2023-02-28 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
