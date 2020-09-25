# Generated by Django 3.1 on 2020-08-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('tittle', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('subtittle', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('Category', models.ManyToManyField(related_name='Category', to='vas3k_test.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
