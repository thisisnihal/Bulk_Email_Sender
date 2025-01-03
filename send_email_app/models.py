from django.db import models

class Employee(models.Model):
    f_Id = models.AutoField(primary_key=True)
    f_Name = models.CharField(max_length=30)
    f_Email = models.EmailField(unique=True)
    f_Designation = models.CharField(max_length=30)

    def __str__(self):
        return f'${self.f_Id} ${self.f_Email}'

