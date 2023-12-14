from django.db import models

# Create your models here.
class Brain(models.Model):
    iq = models.IntegerField()
    weight = models.IntegerField()

class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('female', 'женский'),
        ('think', 'неопределенный'),
        ('figh helicopter', 'боевой вертолет')
    )
    name = models.CharField(max_length=50, default='John')
    sex= models.CharField(max_length=60, choices=SEX)
    brain = models.OneToOneField(
        Brain, 
        on_delete=models.CASCADE,
        related_name='human'
        )