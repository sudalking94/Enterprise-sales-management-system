from django.db import models


class TimeStampedModel(models.Model):
    """만든 일자, 수정일자"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
