# Generated by Django 3.2.5 on 2021-12-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('2', 'ishlatilgan'), ('1', 'yangi'), ('3', 'bepul')], default='1', max_length=10, null=True),
        ),
    ]