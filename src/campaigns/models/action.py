from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .goal import Goal

class Action(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    label = models.CharField(_("label"), max_length=128, null=False, blank=True)
    task = models.TextField(_("task"), null=True, blank=True)
    results = models.TextField(_("results"), null=True, blank=True)
    start_date = models.DateField(_("start date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    deadline = models.DateField(_("deadline"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete_date = models.DateField(_("complete date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(_("complete"), default=False, blank=True)
    goal = models.ForeignKey(Goal, verbose_name=_("goal"), on_delete=models.CASCADE, related_name="goals", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("action")
        verbose_name_plural = _("actions")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("action_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)