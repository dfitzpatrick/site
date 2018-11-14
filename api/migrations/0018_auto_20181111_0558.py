# Generated by Django 2.1.2 on 2018-11-11 05:58

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181029_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakename',
            name='name',
            field=models.CharField(help_text="The regular name for this snake, e.g. 'Python'.", max_length=100, primary_key=True, serialize=False, validators=[]),
        ),
    ]
