# Generated by Django 3.1 on 2020-09-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vas3k_test', '0005_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Category',
        ),
        migrations.AlterField(
            model_name='post',
            name='test',
            field=models.IntegerField(verbose_name=[1]),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('tittle', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('subtittle', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('test', models.IntegerField(verbose_name=[1])),
                ('Category', models.ManyToManyField(related_name='Category', to='vas3k_test.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Заметки',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
