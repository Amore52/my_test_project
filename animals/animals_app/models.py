from wsgiref.validate import validator

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

    SIZE_CHOICES = [TINY, 'Tiny',
                    SMALL, 'Small',
                    MEDIUM, 'Medium',
                    LARGE, 'Large']

    RATING_FIELD = {
        'validators': [
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
    }
    name = models.CharField(max_length=100, verbose_name='Название породы')
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, verbose_name='Размер породы' )
    friendliness = models.IntegerField(verbose_name='Дружелюбность', validators=[
        MinValueValidator(1, message='Значение не может быть меньше 1'),
        MaxValueValidator(5, message='Значение не может быть больше 5')
    ])
    trainability = models.IntegerField(verbose_name='Обучаемость', **RATING_FIELD)
    shedding_amount = models.IntegerField(verbose_name='Интенсивность линьки', **RATING_FIELD)
    exercise_needs = models.IntegerField(verbose_name='Потребность в физической нагрузке', **RATING_FIELD)


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода',
    related_name='animals')
    gender = models.CharField(max_length=1, verbose_name='Пол')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    favorite_food = models.CharField(max_length=255, verbose_name='Любимая еда')
    favorite_toy = models.CharField(max_length=255, verbose_name='Любимые игрушки')



