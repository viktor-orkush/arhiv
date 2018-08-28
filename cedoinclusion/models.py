from django.db import models


class Computers(models.Model):
    serial_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    type = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = 'Компютер'
        verbose_name_plural = 'Компютери'
        ordering = ('serial_number',)


class Cabinets(models.Model):
    id_cabinet = models.ForeignKey(Computers, on_delete=models.CASCADE)
    cabinet_number = models.IntegerField(default=0)

    def __str__(self):
        return self.cabinet_number

    class Meta:
        verbose_name = 'Кабінет'
        verbose_name_plural = 'Кабінети'
        ordering = ('cabinet_number',)


class ComputerTypes(models.Model):
    id_type = models.ForeignKey(Computers, on_delete=models.CASCADE)
    type = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типи'
        ordering = ('type',)


class SedoAllowance(models.Model):
    id_sedo_allowance = models.ForeignKey(Computers, on_delete=models.CASCADE)
    our_income_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    our_income_date = models.DateField(blank=True, null=True, default=None)
    alien_outcome_number = models.CharField(max_length=64, blank=True, null=True, default=None)
    alien_outcome_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.our_income_number

    class Meta:
        verbose_name = 'Включення'
        verbose_name_plural = 'Включення'
        ordering = ('our_income_number',)


class Departments(models.Model):
    id_department = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменти'
        ordering = ('name',)


class Adresses(models.Model):
    id_adress = models.ForeignKey(Departments, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, blank=True, null=True, default=None)
    street = models.CharField(max_length=64, blank=True, null=True, default=None)
    building = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адреси'
        ordering = ('street',)


class Users(models.Model):
    id_cyber_user = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    # id_correspondence = models.ForeignKey(SedoAllowance, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прізвище'
        verbose_name_plural = 'Прізвища'
        ordering = ('name',)


class Ranks(models.Model):
    id_rank = models.ForeignKey(Users, on_delete=models.CASCADE)
    rank = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.rank

    class Meta:
        verbose_name = 'Ранг'
        verbose_name_plural = 'Ранги'
        ordering = ('rank',)