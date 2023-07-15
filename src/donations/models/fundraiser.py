from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from projects.models import Project
from users.models import Member

class Fundraiser(models.Model):
    financial_goal = models.DecimalField(_("financial goal"), max_digits=11, decimal_places=2, null=True, blank=True)
    funds_raised = models.DecimalField(_("funds raised"), default=0, max_digits=11, decimal_places=2, null=True, blank=True)
    closed = models.BooleanField(default=False)
    owner_id = models.PositiveIntegerField(blank=True, null=True)
    owner_content_type = models.OneToOneField(
        ContentType,
        on_delete=models.PROTECT,
    )
    owner = GenericForeignKey(
        fk_field='owner_id',
        ct_field='owner_content_type',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("fundraiser")
        verbose_name_plural = _("fundraisers")

    def __str__(self):
        return f"fundraiser-{self.pk}-{self.created_at}"

    def get_absolute_url(self):
        return reverse("fundraiser_detail", kwargs={"pk": self.pk})
