# Generated by Django 2.0.4 on 2018-04-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CartApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cardNumber',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
