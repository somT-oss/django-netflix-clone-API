from django.db import models


class Plan(models.Model):
    plan_name = models.CharField(max_length=90)
    plan_description = models.CharField(max_length=244)
    stripe_plan_id = models.CharField(max_length=100)

    def __str__(self):
        return self.plan_name


class Price(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def get_display_price(self):
        return f"{self.price / 100}"