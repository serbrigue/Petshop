# Generated by Django 3.2.16 on 2023-08-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_itemcarrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]