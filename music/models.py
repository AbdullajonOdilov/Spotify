from django.db import models

class Singer(models.Model):
    ism = models.CharField(max_length=20)
    t_yil = models.PositiveSmallIntegerField()
    davlat = models.CharField(max_length=20)
    jins = models.CharField(max_length=6)
    def __str__(self):return self.ism
class Albom(models.Model):
    nom = models.CharField(max_length=20)
    yil = models.PositiveSmallIntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    def __str__(self):return f"{self.nom}, {self.singer.ism}"
class Song(models.Model):
    nom = models.CharField(max_length=20)
    albom = models.ForeignKey(Albom,on_delete=models.CASCADE)
    davomiylik = models.DurationField(null=True)
    janr = models.CharField(max_length=10,blank=True)
    mp3_fayl = models.URLField(null=True)
    def __str__(self):return f"{self.nom},{self.albom.nom}"
