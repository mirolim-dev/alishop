# Generated by Django 5.0.6 on 2024-06-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('2', 'ishlatilgan'), ('3', 'bepul'), ('1', 'yangi')], default='1', max_length=10, null=True),
        ),
    ]
