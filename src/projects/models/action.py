from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from users.models import Member

from .project import Project

class Action(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    label = models.CharField(_("label"), max_length=128, null=False, blank=True)
    details = models.TextField(_("details"), null=True, blank=True)
    results = models.TextField(_("results"), null=True, blank=True)
    start_date = models.DateField(_("start date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    clocked_start = models.DateField(_("clocked start"), auto_now=False, auto_now_add=False, null=True, blank=True)
    deadline = models.DateTimeField(_("deadline"), auto_now=False, auto_now_add=False, null=True, blank=True)
    completed_at = models.DateTimeField(_("completed date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(_("complete"), default=False, blank=True)
    assignees = models.JSONField(_("assignees"), default=list, null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="action_plan", null=False, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
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
