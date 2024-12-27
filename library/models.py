import datetime
from django.db import models
from users.models import User
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

PERIOD = [('d', 'день'), ('w', 'неделя'), ('m', 'месяц')]

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя', **NULLABLE)
    surname = models.CharField(max_length=255, verbose_name='фамилия', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')

class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='название', **NULLABLE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='жанр')
    quantity = models.IntegerField(default=1, verbose_name='количество')

    def __str__(self):
        return f'{self.author} - "{self.name}"'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='книга')
    started_at = models.DateTimeField(default= timezone.now, verbose_name='дата начала')
    return_at = models.DateTimeField(
        default=(timezone.now() + datetime.timedelta(days=7)),
        verbose_name='дата возврата')
    is_returned = models.BooleanField(default=False, verbose_name='признак возврата книги')


