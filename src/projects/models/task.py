from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .project import Project

class Task(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    task = models.CharField(_("task"), max_length=128, null=False, blank=True)
    details = models.TextField(_("details"), null=True, blank=True)
    results = models.TextField(_("results"), null=True, blank=True)
    start_date = models.DateField(_("start date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    deadline = models.DateField(_("deadline"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete_date = models.DateField(_("complete date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(_("complete"), default=False, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="tasks", null=False, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='subtasks', on_delete=models.CASCADE)
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