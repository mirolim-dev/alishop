# Generated by Django 5.0.6 on 2024-06-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('1', 'yangi'), ('3', 'bepul'), ('2', 'ishlatilgan')], default='1', max_length=10, null=True),
        ),
    ]