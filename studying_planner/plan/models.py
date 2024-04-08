from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models

class Priority(models.Model):
    priority = models.SmallIntegerField(primary_key=True, verbose_name='Приоритет')
    title = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return f'{self.priority} - {self.title}'


class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Plan(models.Model):

    # PRIORITY_CHOICES = (
    #     (0, 'Срочно пора заняться'),
    #     (1, 'Сразу после важных дел'),
    #     (2, 'Пора бы начать'),
    #     (3, 'Когда-нибудь потом'),
    #     (4, 'В другой жизни'),
    # )

    title = models.CharField(max_length=128, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,
                                 verbose_name='Приоритет')
    time_required = models.FloatField(validators=[MinValueValidator(0.0)],
                                      verbose_name='Примерное время на задачу (в часах)',
                                      blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    # progress = models.IntegerField(validators=[MinValueValidator(0),
    #                                            MaxValueValidator(100)],
    #                                verbose_name='Прогресс',
    #                                blank=True)
    # file = models.FileField()

    class Meta:
        verbose_name = 'план'
        verbose_name_plural = 'Планы'

    def __str__(self):
        return self.title
