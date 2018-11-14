# Generated by Django 2.1.2 on 2018-11-14 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20181112_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakename',
            name='name',
            field=models.CharField(help_text="The regular name for this snake, e.g. 'Python'.", max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(inverse_match=True, regex='^[1-9][0-9]*$')]),
        ),
    ]
