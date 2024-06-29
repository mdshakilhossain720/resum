from django.db import models

# Create your models here.

STATECHOOSE=(
    ('Dhaka','Dhaka'),
    ('Chattogram','Chattogram'),
    ('Dhaka','Dhaka'),
    ('Gazipur','Gazipur'),
    ('Narayanganj','Narayanganj'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),
    ('Dhaka','Dhaka'),

)
class Resum(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(max_length=50,choices=STATECHOOSE,)

    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimage',blank=True)
    filefield=models.FileField(upload_to='doc',blank=True)


