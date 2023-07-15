from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member
from .fundraiser import Fundraiser

class Donation(models.Model):
    donor = models.ForeignKey(Member, verbose_name=_("donor"), on_delete=models.CASCADE, related_name='donations', null=False, blank=True)
    fundraiser = models.ForeignKey(Fundraiser, verbose_name=_("fundraiser"), on_delete=models.CASCADE, related_name='donations', null=False, blank=True)
    amount = models.DecimalField(_("amount"), max_digits=11, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("donation")
        verbose_name_plural = _("donations")

    def __str__(self):
        return f"{self.donor.identity.name} donated ${self.amount} at {self.created_at}"

    def get_absolute_url(self):
        return reverse("donation_detail", kwargs={"pk": self.pk})
