from django.db import models
from core import models as core_models


class Product(core_models.TimeStampedModel):
    """제품 모델"""

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="Product", on_delete=models.CASCADE)
    price = models.models.IntegerField()
    name = models.CharField(max_length=80)


class SalesLog(models.Model):
    """판매 기록 모델"""

    PAY_WAY_CASH = "cash"
    PAY_WAY_CREDIT = "credit"

    PAY_WAY_CHOICES = (
        (PAY_WAY_CASH, "현금"),
        (PAY_WAY_CREDIT, "카드"),
    )

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    pay_way = models.CharField(
        "pay_way", choices=PAY_WAY_CHOICES, max_length=10)