from django.db import models

# Create your models here.

class Sertifikat(models.Model):
    ism_familiya = models.CharField(max_length=255)
    tugilgan_sana = models.DateField()
    sertifikat_rasmi = models.ImageField(upload_to='sertifikatlar/')
    sertifikat_turi = models.CharField(max_length=100)

    def __str__(self):
        return self.ism_familiya