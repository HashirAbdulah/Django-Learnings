# Generated by Django 5.1.1 on 2024-09-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
