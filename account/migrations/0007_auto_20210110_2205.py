# Generated by Django 3.0.4 on 2021-01-10 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210110_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invest_detail',
            name='refer_balance',
        ),
        migrations.RemoveField(
            model_name='invest_detail',
            name='refer_code',
        ),
    ]