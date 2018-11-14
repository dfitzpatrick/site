# Generated by Django 2.1.2 on 2018-11-14 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20181114_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakename',
            name='scientific',
            field=models.CharField(help_text="The scientific name for this snake, e.g. 'Python bivittatus'.", max_length=150, validators=[django.core.validators.RegexValidator(regex='^([^0-9])+')]),
        ),
    ]
