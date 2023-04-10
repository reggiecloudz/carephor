from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .project import Project

class Expenditure(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    item = models.CharField(_("item"), max_length=128, null=False, blank=True)
    purpose = models.TextField(_("purpose"), null=True, blank=True)
    cost = models.DecimalField(_("cost"), max_digits=11, decimal_places=2, null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="expenditures", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("expenditure")
        verbose_name_plural = _("expenditures")

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("expenditure_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.item)
        return super().save(*args, **kwargs)
