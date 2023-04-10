from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .project import Project

class Position(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    title = models.CharField(_("title"), max_length=128, null=False, blank=True)
    details = models.TextField(_("details"), null=True, blank=True)
    open = models.BooleanField(_("open"), default=True)
    people_needed = models.PositiveIntegerField(_("people needed"), default=1, null=False, blank=True)
    positions_filled = models.PositiveIntegerField(_("positions filled"), default=0, null=False, blank=True)
    requirements = models.TextField(_("requirements"), null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="positions", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("position")
        verbose_name_plural = _("positions")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("position_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)