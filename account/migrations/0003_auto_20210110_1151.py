# Generated by Django 3.0.4 on 2021-01-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_invest_detail_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invest_detail',
            name='investment',
            field=models.CharField(choices=[('runing', 'runing'), ('completed', 'completed')], default='running', max_length=200),
        ),
    ]
