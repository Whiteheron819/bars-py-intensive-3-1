from django.db import models

import datetime as dt


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет возвращающий всех сотрудников без директоров
        """

        return super().get_queryset().filter(director__isnull=True)


class Office(models.Model):
    """
    Офис
    """
    address = models.TextField('Адрес')
    mail = models.CharField('Адрес почты', max_length=30,)
    class Meta:
        abstract = True


class EducationOffice(Office):
    """
    Учебный офис
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'education_office'


class GeneralOffice(Office):
    """
    Головной офис
    """
    name = models.TextField('Название головного офиса ')

    class Meta:
        db_table = 'office'


class Department(models.Model):
    """
    Подразделение
    """
    name = models.CharField('Наименование', max_length=30)
    education_office = models.ForeignKey(EducationOffice, on_delete=models.SET_NULL, null=True)
    office = models.ForeignKey(GeneralOffice, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'department'


class Person(models.Model):
    """
    Физическое лицо
    """
    first_name = models.CharField('Фамилия', max_length=30, db_index=True)
    last_name = models.CharField('Имя', max_length=30, db_index=True)

    class Meta:
        abstract = True


class Worker(Person):
    """
    Сотрудник. Если мы не вводим дату выхода на работу, то подставляется текущая дата.
    """
    objects = WorkerManager()
    objects_all = models.Manager()
    startwork_date = models.DateField('Дата выхода на работу', null=True, default=dt.datetime.now())
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_status(self):
        return f'{self.first_name} работает с {self.startwork_date}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'


class OrderedWorker(Worker):
    """
    Модель с  сотрудниками упорядоченными по фамилии и дате приема на работу
    """
    @property
    def startwork_year(self):
        """
        Получить значение года приема на работу
        """
        return self.startwork_date.year

    class Meta:
        proxy = True
        ordering = ['first_name', 'startwork_date']


class Director(Worker):
    """
    Директор
    """
    objects = models.Manager()
    grade = models.IntegerField('Оценка', default=1)

    class Meta:
        db_table = 'directors'
        verbose_name = 'Директор'
