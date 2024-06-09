# Generated by Django 3.2.5 on 2021-11-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=10, null=True),
        ),
    ]
