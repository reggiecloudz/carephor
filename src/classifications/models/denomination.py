from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from churches.choices import BRANCH_CHOICES

class Denomination(models.Model):
    name = models.CharField(_("name"), max_length=100, null=False, blank=True)
    branch = models.CharField(_("branch"), max_length=50, choices=BRANCH_CHOICES, null=False, blank=True)

    class Meta:
        verbose_name = _("denomination")
        verbose_name_plural = _("denominations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("denomination_detail", kwargs={"pk": self.pk})
