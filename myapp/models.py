from django.db import models


# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'

    full_name = models.CharField(verbose_name='ФИО')
    phone = models.CharField(verbose_name='Номер телефона')


class Project(models.Model):
    class Meta:
        verbose_name = 'Объект строительства'
        verbose_name_plural = 'Объекты строительства'

    name = models.CharField(verbose_name='Наименование', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)

    def __str__(self):
        return self.name


class Organization(models.Model):
    class Meta:
        verbose_name = 'Подрядная организация'
        verbose_name_plural = 'Подрядные организации'

    name = models.CharField(verbose_name='Наименование')
    representative = models.ForeignKey('auth.User', verbose_name='Представитель', on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон')
    email = models.CharField(verbose_name='Электронная почта')

    def __str__(self):
        return self.name


class ViolationType(models.Model):
    class Meta:
        verbose_name = 'Тип нарушения'
        verbose_name_plural = 'Классификатор нарушений'

    title = models.CharField(verbose_name='Наименование', max_length=50)

    def __str__(self):
        return self.title


class Violation(models.Model):
    class Meta:
        verbose_name = 'Нарушение'
        verbose_name_plural = 'Нарушения'

    status_types = (
        (0, "Черновик"),
        (1, "Создано"),
        (2, "В работе"),
        (3, "Устранено"),
    )

    title = models.CharField(verbose_name='Наименование', max_length=100)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    status = models.IntegerField(verbose_name='Статус', choices=status_types)
    creator = models.ForeignKey('auth.User', verbose_name='Представитель УСК', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Описание', max_length=500)
    type = models.ForeignKey(ViolationType, verbose_name='Тип нарушения', on_delete=models.CASCADE)
    place = models.CharField(verbose_name='Место', max_length=50)
    project = models.ForeignKey(Project, verbose_name='Объект строительства', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Подрядная организация', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    status_types = (
        (0, 'Черновик'),
        (1, 'Создано'),
        (2, 'В работе'),
        (3, 'Устранено')
    )

    title = models.CharField(verbose_name='Наименование')
    date = models.DateTimeField(verbose_name='Дата постановки', auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Крайний срок')
    status = models.IntegerField(verbose_name='Статус', choices=status_types)
    violation = models.ForeignKey(Violation, verbose_name='Нарушение', on_delete=models.CASCADE)
    creator = models.ForeignKey('auth.User', verbose_name='Постановщик', related_name='created_tasks', on_delete=models.CASCADE)
    executor = models.ForeignKey('auth.User', verbose_name='Исполнитель', related_name='tasks', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Подрядная организация', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class Attachment(models.Model):
    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'

    file = models.FileField(verbose_name='Файл')
    violation = models.ForeignKey(Violation, verbose_name='Нарушение', on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, verbose_name='Комментарий', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.file.name
