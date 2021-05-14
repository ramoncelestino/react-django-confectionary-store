from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=DO_NOTHING)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=CASCADE)
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    complement = models.CharField(max_length=20)

    def __str__(self):
        return self.name;

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,  null=True)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    valuePaid = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return ('{} - {}'.format(self.customer.name, self.createdAt))
