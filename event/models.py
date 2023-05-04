from django.db import models
from django.utils import timezone
# Create your models here.
CHOICES = [("Pending","Pending"),
 ("Started","Started"),
("Completed","Completed")]

class Registered(models.Model):
    Qrid=models.CharField(max_length=100)
    Name=models.CharField(blank=True, max_length=100)
    Points=models.IntegerField(default=0)
    Credits=models.IntegerField(default=300)

    def __str__(self):
        return self.Qrid;

class Games(models.Model):
    Name=models.CharField(max_length=100)
    deduction=models.IntegerField(default=0)
    award=models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class gameRounds(models.Model):
    Name=models.CharField(max_length=100)
    Participants=models.ManyToManyField("Registered", blank=True)
    Game=models.ForeignKey(Games, on_delete=models.CASCADE)
    status=models.CharField(choices=CHOICES, max_length=100, default="Pending")
    Winner=models.CharField(max_length=100, blank=True)
    deduction=models.BooleanField(default=True)

    def __str__(self):
        return self.Name;