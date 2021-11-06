from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class Customer(models.Model):
    """고객 모델"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "기타"),
    )

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="Customers", on_delete=models.CASCADE)
    picture = models.ImageField()
    memo = models.TextField()
    birth = models.DateField(null=True)
    gender = models.CharField("gender", choices=GENDER_CHOICES, max_length=10)
    group = models.ForeignKey(
        "Group", related_name="Customers", on_delete=models.CASCADE)


class Group(core_models.TimeStampedModel):
    """ 고객이 속한 그룹 모델 """

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="Groups", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = (("enterprise", "name"),)

    def __str__(self):
        return self.name
