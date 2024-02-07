from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length= 25)

    def get_absolute_url(self):
        return reverse('home')

class Product(models.Model):
    image= models.ImageField(upload_to= "media")
    name= models.CharField(max_length=25)
    description= models.TextField()
    price= models.IntegerField()
    category= models.TextField()
    commission= models.IntegerField(blank=True, null=True)
    discount= models.IntegerField(blank=True, null=True)
    date= models.DateTimeField(auto_now_add= True)

    def get_absolute_url(self):
        return reverse('home')

class Offer(models.Model):
    product= models.ManyToManyField(Product, blank= True)
    discount_percentage= models.IntegerField()
    valid_till= models.DateField()

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    image= models.ImageField(upload_to= "media", blank=True, null=True)
    name= models.CharField(max_length=25)
    code= models.CharField(max_length=5)
    email= models.EmailField()
    telephone= models.IntegerField()
    earnings= models.IntegerField(default= 0)
    rec_by= models.ForeignKey(User, on_delete= models.CASCADE, related_name= "rec_by", null=True)
    recommendations= models.ManyToManyField(User, blank=True, related_name= "recs")

    def get_absolute_url(self):
        return reverse('home')

class Payment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.CharField(max_length=25)
    amount= models.IntegerField()
    ref= models.CharField(max_length=7)
    transaction= models.CharField(max_length=25, default= "unconfirmed")
    date= models.DateField(auto_now_add= True)

class Bank(models.Model):
    transfer_amount= models.IntegerField()
    transfer_note= models.TextField(blank=True, null=True)
    transfer_reference= models.CharField(max_length=25, blank=True, null=True)
    recipient_code= models.CharField(max_length=25, blank=True, null=True)
    bank_slug= models.CharField(max_length=25, blank=True, null=True)
    bank_code= models.CharField(max_length=25, blank=True, null=True)
    account_name= models.CharField(max_length=25, blank=True, null=True)
    account_number= models.IntegerField(blank=True, null=True)
    email= models.EmailField()

    def get_absolute_url(self):
        return reverse('home')

class Banks(models.Model):
    name= models.CharField(max_length=25)
    code= models.CharField(max_length=25)

class Blog_cat(models.Model):
    name= models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('blog-page')

class Blog(models.Model):
    image= models.ImageField(upload_to= "media")
    title= models.CharField(max_length=25)
    description= models.TextField()
    category= models.CharField(max_length=25)
    pub_date= models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog-page')


