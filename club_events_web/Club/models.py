from django.db import models

# Create your models here.

CLUB_CHOICES=[
    ('Coding Club','Coding Club IITG'),
    ('Electronics','Electroncis Club IITG'),
    ('Robotics','Robotics Club IITG'),
    ('LitSoc','Literary Society IITG'),
    ('Xpressions','Drama Club IITG'),
    ('Aeromodelling','Aeromodelling Club IITG'),
    ('Cadence','Dance Club IITG'),
    ('IITG.AI','Artificial intelligence Club IITG'),
]
class club(models.Model):
    club_name = models.CharField(
        max_length=50,
        choices=CLUB_CHOICES,
        )

    club_secy = models.CharField(max_length=50)


class Post(models.Model):

    club_name = models.ForeignKey(club,on_delete=models.CASCADE)
    updated_on= models.CharField(max_length=50)
    content = models.TextField()
    class Meta:
        ordering=['-updated_on']
    def __str__(self):
        return self.content
