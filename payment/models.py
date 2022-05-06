from django.db import models


class Plan(models.Model):
    plan_name = models.CharField(max_length=90)
    plan_description = models.CharField(max_length=244)

    def __str__(self):
        return self.plan_name


class Price(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.price}"