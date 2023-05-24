
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CheckOut(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.device.name} - {self.employee.username}"
