from django.db import models
from core import models as core_models


class Enterprise(core_models.TimeStampedModel):
    """기업 모델"""

    b_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=80)


class EnterpriseAccessLog(core_models.TimeStampedModel):
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.SET_NULL, null=True)
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    ip = models.CharField(max_length=100)
