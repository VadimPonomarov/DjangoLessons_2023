# Generated by Django 4.2.5 on 2023-10-20 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_profile_profilemodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator('^[A-zА-Я]\\w{2,24}$', 'Name is a string. First letter is capitalized, min 3 max 25 characters')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator('^[A-zА-Я]\\w{2,24}$', 'Name is a string. First letter is capitalized, min 3 max 25 characters')]),
        ),
    ]
