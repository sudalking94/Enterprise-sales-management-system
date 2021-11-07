from django.db import models
from core import models as core_models


class Product(core_models.TimeStampedModel):
    """제품 모델"""

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="products", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def won_price(self):
        price = f'{self.price:,}' + "원"
        return price


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
    pay_way = models.CharField(
        "pay_way", choices=PAY_WAY_CHOICES, max_length=10)
