# Generated by Django 3.2.5 on 2021-12-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0013_orderproduct_reduced_price_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='pochta_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
