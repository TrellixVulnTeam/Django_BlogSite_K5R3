# Generated by Django 2.2.7 on 2019-11-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20191124_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim'),
        ),
    ]
