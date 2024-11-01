# Generated by Django 5.1.2 on 2024-10-27 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='Your name must contain minimum 4 letters'), django.core.validators.RegexValidator(message='Your name must contain letters only!', regex='^[A-Za-z]+$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Your name must contain minimum 4 letters'), django.core.validators.RegexValidator(message='Your name must contain letters only!', regex='^[A-Za-z]+$')])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits.', max_length=6, validators=[django.core.validators.RegexValidator(message='Your passcode must be exactly 6 digits!', regex='^\\d{6}$')])),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]