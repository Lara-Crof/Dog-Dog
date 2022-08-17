# Generated by Django 4.0.5 on 2022-06-24 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findhouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_animal', models.CharField(choices=[('CAT', 'Котик'), ('DOG', 'Собачка')], default='CAT', max_length=3, verbose_name='Тип животного')),
            ],
        ),
        migrations.AlterModelOptions(
            name='helps_of_animals',
            options={'ordering': ['-time_assistance'], 'verbose_name': 'Тип помощи', 'verbose_name_plural': 'Тип помощи'},
        ),
        migrations.AddField(
            model_name='findhome',
            name='actualish',
            field=models.BooleanField(default=True, verbose_name='Акнтуальность'),
        ),
        migrations.AddField(
            model_name='findhome',
            name='health',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='findhouse.health_level'),
        ),
        migrations.AddField(
            model_name='findhome',
            name='helps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='findhouse.helps_of_animals'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(choices=[('M', 'Мальчик'), ('F', 'Девочка')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='helps_of_animals',
            name='title',
            field=models.CharField(choices=[('shelter', 'Ищит дом'), ('funds_for_treatment', 'Временная передержка'), ('temporary_overexposure', 'Требуеться лечение')], max_length=40, verbose_name='Тип помощи'),
        ),
        migrations.AddField(
            model_name='findhome',
            name='animals',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='findhouse.animals'),
        ),
    ]
