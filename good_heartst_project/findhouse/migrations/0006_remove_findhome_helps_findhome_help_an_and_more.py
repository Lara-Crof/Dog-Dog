# Generated by Django 4.0.5 on 2022-06-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhouse', '0005_remove_health_level_gender_findhome_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='findhome',
            name='helps',
        ),
        migrations.AddField(
            model_name='findhome',
            name='help_an',
            field=models.CharField(choices=[('shelter', 'Ищит дом'), ('funds_for_treatment', 'Временная передержка'), ('temporary_overexposure', 'Требуеться лечение')], default='shelter', max_length=40, verbose_name='Тип помощи'),
        ),
        migrations.RemoveField(
            model_name='findhome',
            name='gender',
        ),
        migrations.AddField(
            model_name='findhome',
            name='gender',
            field=models.CharField(choices=[('M', 'Мальчик'), ('F', 'Девочка')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='findhome',
            name='health',
            field=models.CharField(choices=[('1', 'Полностью здоров'), ('2', 'Нуждаеться в легком лечение'), ('3', 'Нуждается в лечение'), ('4', 'Требуеться операция'), ('5', 'Мы с Вами вылечили его благодарая Вашей помощи')], default='1', max_length=40),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Health_level',
        ),
    ]
