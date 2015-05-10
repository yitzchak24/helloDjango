from django.db import models

class Hello(models.Model):
    title =models.CharField(max_length=100)
    author = models.CharField(max_length=75)
    read = models.CharField(max_length=5)
    def __unicode__(self):
        return self.title + " / " + self.author + " / " + self.read