from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    description = models.TextField()
    image_path = models.ImageField(upload_to='animal_images/')
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Adopted', 'Adopted'),
        ('Fostered', 'Fostered'),
        ('Adoption Pending', 'Adoption Pending'),
    ]
    status = models.CharField(max_length=19, choices=STATUS_CHOICES)
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Request for {self.animal.name} by {self.user.username}"
