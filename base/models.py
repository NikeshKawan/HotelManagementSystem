from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
user_type_list = [('Frontdesk', 'Frontdesk'), ('Restaurant', 'Restaurant'), ('Accounting', 'Accounting'), ('Management','Management')]

room_status_list = [('Available', 'Available'), ('Unavailable', 'Unavailable')]

gender_list = [('Male','Male'), ('Female', 'Female'),('Others', 'Others')]

bill_status = [('paid', 'paid'), ('unpaid', 'unpaid')]

payment_method_list = [('cash','cash'),('online payment','online payment')]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='User',null=True)
    user_type = models.CharField(max_length=20, choices=user_type_list)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']
    


class RoomType(models.Model):
    name = models.CharField(max_length = 200)


class Room(models.Model):
    name = models.CharField(max_length = 200)
    room_no = models.BigIntegerField()
    bed_count = models.IntegerField()
    status = models.CharField(max_length=200, choices=room_status_list)
    room_type = models.ForeignKey(RoomType,on_delete= models.SET_NULL,null=True)


class EmployeeInfo(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length = 200, choices= gender_list)
    joining_date = models.DateField()
    salary = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)



class CustomerDetails(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    address = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 200, choices=gender_list)
    work = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    room = models.ForeignKey(Room,on_delete= models.SET_NULL, null=True)


class Bill(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    amount = models.IntegerField()
    status = models.CharField(max_length = 200, choices=bill_status )
    customer_detail = models.ForeignKey(CustomerDetails,on_delete=models.SET_NULL,null=True)

class MenuType(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    name = models.CharField(max_length = 200)
    ingredients = models.TextField()
    food_type = models.CharField(max_length = 200)
    price = models.IntegerField()
    menu_type = models.ForeignKey(MenuType,on_delete=models.SET_NULL,null=True)


class PaymentInfo(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.SET_NULL,null=True)
    paid_amount = models.IntegerField()
    payment_method = models.CharField(max_length=200, choices= payment_method_list)



class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Facilities(models.Model):
    name = models.CharField(max_length=200)
    description= models.TextField()
