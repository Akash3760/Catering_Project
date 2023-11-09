from datetime import timezone

from django.core.validators import RegexValidator, EmailValidator
from django.db import models


# Create your models here.
class BookNow(models.Model):
    Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55, validators=[EmailValidator(message="Enter a valid email address.")])
    Number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")]
    )
    Enquiry = models.CharField(max_length=20)
    Person = models.CharField(max_length=15)


class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=55, validators=[EmailValidator(message="Enter a valid email address.")])
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class Menu(models.Model):
    CATEGORY_CHOICES = (
        ('Chicken Items', 'Chicken Items'),
        ('Mutton Items', 'Mutton Items'),
        ('Fish Items', 'Fish Items'),
        ('Dal', 'Dal'),
        ('Rice', 'Rice'),
        ('Flourbased', 'Flourbased'),
        ('Veg Menu', 'Veg Menu'),
        ('Snacks', 'Snacks'),
        ('Sweets', 'Sweets'),
        ('Drinks', 'Drinks'),
        ('Salads', 'Salads'),
        ('Papad', 'Papad'),
        ('Chutney', 'Chutney'),
    )

    name = models.CharField(max_length=100)
    menu = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Veg Menu')

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
