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


class ContestYear(models.Model):
    year = models.IntegerField('Рік')

    objects = models.Manager()

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Олімпіадний рік'
        verbose_name_plural = 'Олімпіадні роки'


class Winner(models.Model):
    GOLD = 'gl'
    SILVER = 'sl'
    BRONZE = 'bz'
    PLACE_CHOICES = (
        (GOLD, 'I'),
        (SILVER, 'II'),
        (BRONZE, 'III')
    )
    STAGE1 = 's1'
    STAGE2 = 's2'
    STAGE3 = 's3'
    STAGE_CHOICES = (
        (STAGE1, 'II (районний) етап'),
        (STAGE2, 'III (обласний) етап'),
        (STAGE3, 'II (обласний) етап МАН')
    )

    subject = models.CharField('Предмет', max_length=20)
    
    stage = models.CharField(
        'Етап',
        max_length=2,
        choices=STAGE_CHOICES,
        default='s1'
    )

    first_name = models.CharField("Ім'я", max_length = 20)
    second_name = models.CharField('Прізвище', max_length = 20)
    year = models.ForeignKey(ContestYear, on_delete=models.CASCADE)
    class_n = models.CharField("Клас", max_length = 20)
    teacher = models.CharField("Вчитель", max_length = 20)
    place = models.CharField(
        'Місце',
        max_length=2,
        choices=PLACE_CHOICES,
        default='gl'
    )


    def get_name(self):
        return self.first_name + ' ' + self.second_name

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name = 'Переможець'
        verbose_name_plural = 'Переможці'