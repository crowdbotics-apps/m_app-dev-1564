# Generated by Django 2.2.9 on 2020-01-31 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customtext_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customtext',
            name='test',
        ),
    ]
