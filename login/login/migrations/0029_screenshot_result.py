# Generated by Django 2.1 on 2019-02-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0028_auto_20190218_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='result',
            field=models.TextField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
