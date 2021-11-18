from django.db import models
from django.urls import reverse
from core import models as core_models


class Product(core_models.TimeStampedModel):
    """제품 모델"""

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="products", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    memo = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_memo(self):
        if len(self.memo[:10]) == 10:
            result = self.memo[0:10] + '...'
        else:
            result = self.memo
        return result

    def won_price(self):
        price = f'{self.price:,}' + "원"
        return price

    def get_delete_url(self):
        return reverse("products:delete-product", kwargs={"id": self.pk})


class SalesLog(core_models.TimeStampedModel):
    """판매 기록 모델"""

    PAY_WAY_CASH = "cash"
    PAY_WAY_CREDIT = "credit"

    PAY_WAY_CHOICES = (
        (PAY_WAY_CASH, "현금"),
        (PAY_WAY_CREDIT, "카드"),
    )

    enterprise = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    memo = models.TextField(blank=True)
    pay_way = models.CharField(
        "pay_way", choices=PAY_WAY_CHOICES, max_length=10)

    def get_memo(self):
        if len(self.memo[:10]) == 10:
            result = self.memo[:10] + '...'
        else:
            result = self.memo
        return result

    def won_price(self):
        price = f'{self.price:,}' + "원"
        return price

    def get_delete_url(self):
        return reverse("products:delete-sales", kwargs={"id": self.id})
