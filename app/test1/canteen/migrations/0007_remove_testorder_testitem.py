# Generated by Django 2.2.2 on 2019-11-15 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0006_insert_initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testorder',
            name='testItem',
        ),
    ]