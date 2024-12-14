from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name 

class Order(models.Model):
    items = models.ManyToManyField(MenuItem, through='OrderItem')  # Many-to-Many through relationship
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100,null=True, blank=True)  # Add user name field

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
