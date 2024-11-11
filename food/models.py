from django.db import models

# Create your models here.




class food(models.Model):
    x=[
        ('drinks','drinks'),
        ('lunch','lunch'),
        ('dinner','dinner'),

    ]
    name= models.CharField(max_length=50)
    description = models.TextField()
    price= models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    category= models.CharField(max_length=50 ,null=True, choices=x )


    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']
        verbose_name= 'Menu'



