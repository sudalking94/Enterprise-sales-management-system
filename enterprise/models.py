from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from core import models as core_models
from core import managers as core_managers


class Enterprise(AbstractBaseUser, PermissionsMixin):
    """기업 모델"""

    name_validator = UnicodeUsernameValidator()

    b_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    name = models.CharField(
        max_length=150,
        unique=True,
        validators=[name_validator],
        error_messages={
            'unique': "A user with that name already exists.",
        },
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.',
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
    objects = core_managers.CustomUserManager()

    class Meta:
        verbose_name = "Enterprise"


class EnterpriseAccessLog(core_models.TimeStampedModel):
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.SET_NULL, null=True)
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    ip = models.CharField(max_length=100)
