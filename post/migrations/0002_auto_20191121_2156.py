# Generated by Django 2.2.7 on 2019-11-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='publishDate',
            field=models.DateField(auto_now_add=True, verbose_name='Yayınlanma Tarihi'),
        ),
    ]
