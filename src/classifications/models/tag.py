from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from classifications.models import Cause

class Tag(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    name = models.CharField(_("name"), max_length=128, null=False, blank=True)
    cause = models.ForeignKey(Cause, verbose_name=_("cause"), on_delete=models.CASCADE, related_name="tags", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
