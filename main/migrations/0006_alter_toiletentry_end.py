# Generated by Django 4.2.13 on 2024-07-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_toiletentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toiletentry',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
    ]
