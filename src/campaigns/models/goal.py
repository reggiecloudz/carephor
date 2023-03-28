from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .campaign import Campaign

class Goal(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    name = models.CharField(_("name"), max_length=128, null=False, blank=True)
    details = models.TextField(_("details"), null=True, blank=True)
    results = models.TextField(_("results"), null=True, blank=True)
    start_date = models.DateField(_("start date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    deadline = models.DateField(_("deadline"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete_date = models.DateField(_("complete date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(_("complete"), default=False, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"), on_delete=models.CASCADE, related_name="goals", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("goal")
        verbose_name_plural = _("goals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("goal_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)