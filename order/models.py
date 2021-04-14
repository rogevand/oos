from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument1 = models.CharField(max_length=50, null=True, blank=True)
    instrument2 = models.CharField(max_length=50, null=True, blank=True)
    vocalYN = models.BooleanField()

    def __str__(self):
        return self.name
    
class Hymn(models.Model):
    name = models.CharField(max_length=50)
    book = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Service(models.Model):
    date = models.DateField()
    leader =  models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    prelude_time = models.TimeField()
    sermon = models.CharField(max_length=50)
    announcements = models.CharField(max_length=50)
    musicians = models.ManyToManyField(Musician)
    hymns = models.ManyToManyField(Hymn)

    def __str__(self):
        return str(self.date)






