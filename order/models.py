from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument1 = models.CharField(max_length=50, null=True, blank=True)
    instrument2 = models.CharField(max_length=50, null=True, blank=True)
    vocalYN = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Hymn(models.Model):
    name = models.CharField(max_length=50)
    book = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    date = models.CharField(max_length=50, null=True, blank=True)
    leader =  models.CharField(max_length=50, null=True, blank=True)
    theme = models.CharField(max_length=50, null=True, blank=True)
    prelude_time = models.CharField(max_length=50, null=True, blank=True)
    sermon = models.CharField(max_length=50, null=True, blank=True)
    announcements = models.CharField(max_length=50, null=True, blank=True)
    #there are two pianists and a special and 3 hymns
    musician = models.ManyToManyField(Musician, blank=True)
    hymn = models.ManyToManyField(Hymn, blank=True)
    special = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.date)






