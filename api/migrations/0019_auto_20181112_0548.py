# Generated by Django 2.1.2 on 2018-11-12 05:48

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20181111_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakename',
            name='scientific',
            field=models.CharField(help_text="The scientific name for this snake, e.g. 'Python bivittatus'.", max_length=150, validators=[]),
        ),
    ]
