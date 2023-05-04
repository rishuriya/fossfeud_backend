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
    gameAward=models.ForeignKey("Award", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name

class gameRounds(models.Model):
    Name=models.CharField(max_length=100)
    Participants=models.ManyToManyField("Registered", blank=True)
    Game=models.ForeignKey(Games, on_delete=models.CASCADE)
    status=models.CharField(choices=CHOICES, max_length=100, default="Pending")
    Winner=models.ForeignKey("winners", on_delete=models.CASCADE, blank=True, null=True)
    deduction=models.BooleanField(default=True)

    def __str__(self):
        return self.Name;

class winners(models.Model):
    roundId=models.ForeignKey(gameRounds, on_delete=models.CASCADE,blank=True)
    gameId=models.ForeignKey(Games, on_delete=models.CASCADE,blank=True,null=True)
    firstPlace=models.CharField(max_length=100, blank=True)
    secondPlace=models.CharField(max_length=100, blank=True)
    thirdPlace=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.roundId.Name
    
class Award(models.Model):
    gameId=models.ForeignKey(Games, on_delete=models.CASCADE,blank=True)
    firstPlace=models.IntegerField(blank=True)
    secondPlace=models.IntegerField(blank=True)
    thirdPlace=models.IntegerField(blank=True)

    def __str__(self):
        return self.gameId.Name