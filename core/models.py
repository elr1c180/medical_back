from django.db import models

class Doctor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Medication(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Procedure(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='procedures')
    date = models.DateField()
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='procedures')

    def __str__(self):
        return self.name
