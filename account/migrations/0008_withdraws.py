# Generated by Django 3.0.4 on 2021-01-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210110_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdraws',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_email', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('withdraw_amount', models.FloatField(max_length=100)),
                ('status', models.CharField(blank=True, choices=[('success', 'success'), ('pending', 'pending')], max_length=100, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]