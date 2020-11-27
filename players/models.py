from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    base_salary = models.DecimalField(max_digits=14, decimal_places=2)
    guaranteed_compensation = models.DecimalField(
        max_digits=14, decimal_places=2)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    positions = models.ManyToManyField(Position)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
