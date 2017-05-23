from django.db import models
from django.utils import timezone
from django.conf import settings



class Category(models.Model):
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	title = models.CharField(max_length=30, verbose_name='Название', unique=True)

	def __str__(self):
		return self.title



class Mesage(models.Model):
	class Meta():
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'

	name = models.CharField(max_length=30, verbose_name='Имя:')
	email = models.EmailField(verbose_name='Почт. ящик:')
	text = models.TextField(verbose_name='Сообщение:')

	def __str__(self):
		return self.name



class PortfolioItem(models.Model):
	class Meta():
		verbose_name = 'Работа'
		verbose_name_plural = 'Работы'

	category = models.ManyToManyField(Category, verbose_name='Категория(и):')
	title = models.CharField(max_length=200, verbose_name='Название:')
	description = models.TextField(verbose_name='Описание:')
	img_small = models.ImageField(upload_to='portfolio/%d-%m-%Y', verbose_name='Мал. изображение:')
	img_big = models.ImageField(upload_to='portfolio/%d-%m-%Y', verbose_name='Бол. изображение:')
	project_url = models.URLField(max_length=200, verbose_name='Ссылка проекта:')
	download = models.URLField(max_length=300, verbose_name='Ссылка скачки:')
	created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания:')
	published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации:')
	likes = models.IntegerField(default=0, verbose_name='Кол. лайков:')
	previews = models.IntegerField(default=0, verbose_name='Кол. просмотров:')

	def __str__(self):
		return self.title
