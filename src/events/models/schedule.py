from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from .event import Event

class Schedule(models.Model):
    # { label, startby, finishby, details, created_at }
    entries = models.JSONField(_("entries"), default=list, null=True, blank=True)
    event = models.OneToOneField(Event, verbose_name=_("event"), on_delete=models.CASCADE, related_name='schedule', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")

    def __str__(self):
        return f"{self.event.name} schedule"

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})
