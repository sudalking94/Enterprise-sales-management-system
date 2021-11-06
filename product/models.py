from django.db import models
from core import models as core_models


class Product(core_models.TimeStampedModel):
    """제품 모델"""

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="products", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class SalesLog(core_models.TimeStampedModel):
    """판매 기록 모델"""

    PAY_WAY_CASH = "cash"
    PAY_WAY_CREDIT = "credit"

    PAY_WAY_CHOICES = (
        (PAY_WAY_CASH, "현금"),
        (PAY_WAY_CREDIT, "카드"),
    )

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", on_delete=models.SET_NULL, null=True, related_name="sales_logs")
    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.SET_NULL, null=True, related_name="sales_logs")
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="sales_logs")
    pay_way = models.CharField(
        "pay_way", choices=PAY_WAY_CHOICES, max_length=10)
