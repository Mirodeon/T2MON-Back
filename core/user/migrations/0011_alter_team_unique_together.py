# Generated by Django 4.1 on 2022-11-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0010_alter_bag_order_alter_petstore_order_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set(),
        ),
    ]
