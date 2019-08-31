from django.db import models

class AllMedalist(models.Model):
    year = models.IntegerField('Рік')

    objects = models.Manager()

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Медалісти'
        verbose_name_plural = 'Медалісти'


class Medalist(models.Model):
    GOLD = 'gl'
    SILVER = 'sl'
    MEDALIST_CHOICES = (
        (GOLD, 'Золотий медаліст'),
        (SILVER, 'Срібний медаліст')
    )

    first_name = models.CharField("Ім'я", max_length = 20)
    second_name = models.CharField('Прізвище', max_length = 20)
    year = models.ForeignKey(AllMedalist, on_delete=models.CASCADE)
    medalist_type = models.CharField(
        'Тип медаліста',
        max_length=2,
        choices=MEDALIST_CHOICES,
        default='gl'
    )

    def get_name(self):
        return self.first_name + ' ' + self.second_name


    def __str__(self):
        return self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name = 'Медаліст'
        verbose_name_plural = 'Медалісти'
