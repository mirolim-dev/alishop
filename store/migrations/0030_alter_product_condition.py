# Generated by Django 5.0.6 on 2024-06-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('3', 'bepul'), ('1', 'yangi'), ('2', 'ishlatilgan')], default='1', max_length=10, null=True),
        ),
    ]