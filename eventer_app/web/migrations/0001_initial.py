# Generated by Django 3.2.20 on 2023-08-16 06:18

import django.core.validators
from django.db import migrations, models
import eventer_app.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, validators=[eventer_app.web.validators.validate_sting_contains_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinValueValidator(4)])),
                ('email', models.EmailField(max_length=45)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(5)])),
            ],
        ),
    ]