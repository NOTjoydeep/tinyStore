# Generated by Django 4.1.1 on 2022-09-05 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0014_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
