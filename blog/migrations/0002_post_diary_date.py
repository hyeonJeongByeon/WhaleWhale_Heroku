# Generated by Django 2.2.1 on 2019-06-29 21:29

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='diary_date',
            field=models.DateField(default=django.utils.timezone.now, validators=[blog.models.no_future]),
            preserve_default=False,
        ),
    ]
