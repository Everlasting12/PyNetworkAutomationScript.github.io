# Generated by Django 3.1.7 on 2021-04-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210324_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
