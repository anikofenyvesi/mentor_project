from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)
    
class Opinion(models.Model):
    question = models.ForeignKey(Mentor)
    name = models.CharField(max_length=50)
    description = models.TextField()
