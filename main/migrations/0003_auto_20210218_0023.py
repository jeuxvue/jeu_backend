# Generated by Django 3.1.6 on 2021-02-17 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210218_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'managed': False, 'verbose_name': 'Games'},
        ),
        migrations.AlterModelTable(
            name='games',
            table='game',
        ),
    ]