from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Studend(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=30)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.guruh

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(default=True)
    kitoblar_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism



class Kitob(models.Model):
    JANR = (
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli"),
        ("Detektiv", "Detektiv"),
            )
    nom = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=12, choices=JANR)
    sana = models.DateField()
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom

class Record(models.Model):
    sana = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    qaytardi = models.CharField(max_length=5, choices=(("Ha", "Ha"), ("Yo'q", "Yo'q")))
    qaytarish_sana = models.DateField(blank=True,null=True)
    def __str__(self):
        return f"{self.student.ism},{self.kitob.nom}"


class Kutubxonachi(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    foydalanuvchi = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism




































