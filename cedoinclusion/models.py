from django.db import models


# class ComputerTypes(models.Model):
#     type = models.CharField(max_length=64, blank=True, null=True, default=None)
#
#     def __str__(self):
#         return self.type
#
#     class Meta:
#         verbose_name = 'Тип'
#         verbose_name_plural = 'Типи'
#         ordering = ('type',)


class Adresses(models.Model):
    military_number = models.CharField(max_length=16, blank=True, null=True, default=None)
    city = models.CharField(max_length=64, blank=True, null=True, default=None)
    street = models.CharField(max_length=64, blank=True, null=True, default=None)
    building = models.CharField(max_length=64, blank=True, null=True, default=None)

    # def __str__(self):
    #     return self.city

    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адреси'
        ordering = ('street',)


class Departments(models.Model):
    adress = models.ForeignKey(Adresses, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменти'
        ordering = ('name',)


class Ranks(models.Model):
    rank = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.rank

    class Meta:
        verbose_name = 'Ранг'
        verbose_name_plural = 'Ранги'
        ordering = ('rank',)


class Personal(models.Model):
    # id_cyber_user = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    # id_worker = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    rank = models.ForeignKey(Ranks, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ('name',)


class OfficersAdminsSedo(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офіцер ЦАБ'
        verbose_name_plural = 'Офіцери ЦАБ'
        ordering = ('name',)


class SedoAllowance(models.Model):
    # id = models.AutoField(primary_key=True)
    our_income_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    our_income_date = models.DateField(blank=True, null=True, default=None)
    alien_outcome_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    alien_outcome_date = models.DateField(blank=True, null=True, default=None)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    CAB_officer = models.ForeignKey(OfficersAdminsSedo, related_name='CAB_officer', on_delete=models.DO_NOTHING, null=True, blank=True)
    cyber_user = models.ForeignKey(Personal, related_name='cyber_user', on_delete=models.DO_NOTHING, null=True, blank=True)
    worker_user = models.ForeignKey(Personal, related_name='worker_user', on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Включення'
        verbose_name_plural = 'Включення'
        ordering = ('id',)


class Computers(models.Model):
    sedo_allowance = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    type = models.CharField(max_length=64, blank=True, null=True, default=None)
    cabinet_number = models.CharField(max_length=8, blank=True, default=0)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Компютер'
        verbose_name_plural = 'Компютери'
        ordering = ('id',)