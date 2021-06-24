# Generated by Django 3.1.7 on 2021-03-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210320_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_name', models.CharField(max_length=50)),
                ('script_author', models.CharField(max_length=30)),
                ('script_file', models.FileField(upload_to='media')),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
