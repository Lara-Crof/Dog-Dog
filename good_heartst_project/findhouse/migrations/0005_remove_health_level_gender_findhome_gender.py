# Generated by Django 4.0.5 on 2022-06-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhouse', '0004_remove_findhome_animals_findhome_type_animal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health_level',
            name='gender',
        ),
        migrations.AddField(
            model_name='findhome',
            name='gender',
            field=models.ManyToManyField(to='findhouse.gender'),
        ),
    ]