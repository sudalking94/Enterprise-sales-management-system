from django.db import models
from django.urls import reverse
from core import models as core_models


class Customer(core_models.TimeStampedModel):
    """고객 모델"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "기타"),
    )

    name = models.CharField(max_length=50)
    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="customers", on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, upload_to='static/avatars')
    memo = models.TextField(blank=True)
    birth = models.DateField()
    gender = models.CharField("gender", choices=GENDER_CHOICES, max_length=10)
    group = models.ForeignKey(
        "Group", related_name="customers", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customers:detail-customer", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("customers:edit-customer", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("customers:delete-customer", kwargs={"id": self.id})


class Group(core_models.TimeStampedModel):
    """ 고객이 속한 그룹 모델 """

    enterprise = models.ForeignKey(
        "enterprise.Enterprise", related_name="customer_groups", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = (("enterprise", "name"),)

    def __str__(self):
        return self.name
