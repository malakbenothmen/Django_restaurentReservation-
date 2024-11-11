from django.db import models

# Create your models here.
class Reservation(models.Model):
    x=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    ]

    cin = models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    email= models.EmailField()
    numtel = models.CharField(max_length=15)
    nbPersonne = models.CharField(max_length=2,default=1, choices=x)
  
    date=models.DateField()
    time=models.TimeField(null=True)



    def __str__(self):
        return "%s" %(self.username)

    class Meta:
        db_table="reservation" 



