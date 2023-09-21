from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class Worker(AbstractUser):

    phone = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='worker_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='worker_user_permissions',
    )

    def __str__(self):
        return self.username
