# Generated by Django 2.2.2 on 2019-12-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0005_delete_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_order',
            name='status',
            field=models.CharField(choices=[('o', 'ordered'), ('p', 'paid'), ('a', 'approved'), ('c', 'canceled'), ('d', 'delivered')], default='o', max_length=1),
        ),
    ]
