from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    phonenumber = models.CharField(max_length=11, default='')
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    COURSE_LEVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    course_code = models.CharField(
        max_length=10
    )

    description = models.CharField(
        max_length=100
    )

    level = models.CharField(
        max_length=1, 
        choices=COURSE_LEVEL, 
        blank=False, 
        null=False,
        default='B',
    )

    def __str__(self):
        return self.description


class Registration(models.Model):
    PERIOD = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
        ('I', 'Integral'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )

    period = models.CharField(
        max_length=1,
        choices=PERIOD,
        blank=False,
        null=False,
        default='I',
    )
