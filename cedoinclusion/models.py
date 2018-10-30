from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=64, blank=True)
    military_number = models.CharField(max_length=16, blank=True, null=True, default=None)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64, blank=True, null=True, default=None)
    building = models.CharField(max_length=64, blank=True, null=True, default=None)


    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменти'
        ordering = ('name',)


class Ranks(models.Model):
    rank = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.rank

    class Meta:
        verbose_name = 'Ранг'
        verbose_name_plural = 'Ранги'
        ordering = ('rank',)


class Personal(models.Model):
    rank = models.ForeignKey(Ranks, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ('name',)


class OfficersAdminsSedo(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офіцер ЦАБ'
        verbose_name_plural = 'Офіцери ЦАБ'
        ordering = ('name',)


class SedoAllowances(models.Model):
    our_income_number = models.CharField(max_length=64, blank=True)
    our_income_date = models.DateField(blank=True, null=True)
    alien_outcome_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    alien_outcome_date = models.DateField(blank=True, null=True, default=None)
    department = models.ForeignKey(Departments, blank=True, on_delete=models.CASCADE)
    CAB_officer = models.ForeignKey(OfficersAdminsSedo, related_name='CAB_officer', on_delete=models.DO_NOTHING)
    cyber_user = models.ForeignKey(Personal, related_name='cyber_user', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Включення'
        verbose_name_plural = 'Включення'
        ordering = ('id',)


class Computers(models.Model):
    sedo_allowance = models.ForeignKey(SedoAllowances, blank=True, null=True, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    ip = models.GenericIPAddressField(blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True, default=None)
    cabinet_number = models.CharField(max_length=8, blank=True, default=0)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Компютер'
        verbose_name_plural = 'Компютери'
        ordering = ('id',)