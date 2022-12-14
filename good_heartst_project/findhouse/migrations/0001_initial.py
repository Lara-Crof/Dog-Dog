# Generated by Django 4.0.5 on 2022-06-24 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FindHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locations_comment', models.TextField(blank=True, verbose_name='Короткое описание места')),
                ('age', models.CharField(max_length=25, verbose_name='примерный возрасту ')),
                ('description', models.TextField(help_text='Расскажите о крохе', verbose_name='История животного')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='animals/%Y/%m/%d/', verbose_name='Фото животных которым нужен дом')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_up', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Опубликовать')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Мальчик'), ('F', 'Девочка')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Helps_of_animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Тип помощи')),
                ('time_assistance', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Health_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.CharField(choices=[('1', 'Полностью здоров'), ('2', 'Нуждаеться в легком лечение'), ('3', 'Нуждается в лечение'), ('4', 'Требуеться операция'), ('5', 'Мы с Вами вылечили его благодарая Вашей помощи')], default='1', max_length=40)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='findhouse.gender')),
            ],
        ),
    ]
