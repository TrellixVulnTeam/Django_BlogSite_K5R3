# Generated by Django 2.2.7 on 2019-11-25 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20191126_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postcomment2',
            new_name='postcomment',
        ),
    ]
