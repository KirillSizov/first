from datetime import datetime

from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    """Пост"""
    picture = models.ImageField("Картинка")
    name = models.CharField("Название", max_length=150)
    tittle = models.CharField("Заголовок", max_length=150)
    subtittle = models.CharField("Подзаголовок", max_length=150)
    text = models.TextField("Текст")
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    test = models.IntegerField([1])
    draft = models.BooleanField("Черновик", default=False)
    date = models.DateField("Дата публикации", default=datetime.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Travel(models.Model):
    """Путешествия"""
    picture = models.ImageField("Картинка")
    name = models.CharField("Название", max_length=150)
    tittle = models.CharField("Заголовок", max_length=150)
    subtittle = models.CharField("Подзаголовок", max_length=150)
    text = models.TextField("Текст")
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    test = models.IntegerField([1])
    draft = models.BooleanField("Черновик", default=False)
    date = models.DateField("Дата публикации", default=datetime.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("travel_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Путешествия"
        verbose_name_plural = "Путешествия"


class Notes(models.Model):
    """Заметки"""
    picture = models.ImageField("Картинка")
    name = models.CharField("Название", max_length=150)
    tittle = models.CharField("Заголовок", max_length=150)
    subtittle = models.CharField("Подзаголовок", max_length=150)
    text = models.TextField("Текст")
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    test = models.IntegerField([1])
    draft = models.BooleanField("Черновик", default=False)
    date = models.DateField("Дата публикации", default=datetime.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("notes_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Заметки"
        verbose_name_plural = "Заметки"


class Challenge(models.Model):
    """Заметки"""
    picture = models.ImageField("Картинка")
    name = models.CharField("Название", max_length=150)
    tittle = models.CharField("Заголовок", max_length=150)
    subtittle = models.CharField("Подзаголовок", max_length=150)
    text = models.TextField("Текст")
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    test = models.IntegerField([1])
    draft = models.BooleanField("Черновик", default=False)
    date = models.DateField("Дата публикации", default=datetime.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("challenge_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Челлендж"
        verbose_name_plural = "Челленджи"
