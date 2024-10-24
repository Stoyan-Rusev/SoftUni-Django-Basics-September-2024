# Generated by Django 5.1.1 on 2024-10-15 06:30

import forumApp.posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[forumApp.posts.validators.BadLanguageValidator()]),
        ),
        migrations.AlterField(
            model_name='post',
            name='languages',
            field=models.CharField(choices=[('py', 'Python'), ('js', 'Javascript'), ('j', 'Java'), ('c', 'C'), ('cpp', 'C++'), ('cs', 'C#'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
