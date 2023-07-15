from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member
from events.models import Event
from classifications.models import Cause

class Project(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    name = models.CharField(_("name"), max_length=128, null=False, blank=True)
    photo = models.ImageField(upload_to='projects/%Y/%m/%d/', null=True, blank=True)
    closed = models.BooleanField(default=False)
    manager = models.ForeignKey(Member, verbose_name=_("manager"), on_delete=models.CASCADE, related_name="projects_managed", null=True, blank=True)
    cause = models.ForeignKey(Cause, verbose_name=_("cause"), on_delete=models.CASCADE, related_name="projects", null=False, blank=True)
    members = models.ManyToManyField(Member, related_name="projects", through="ProjectMember", blank=True)
    events = GenericRelation(Event, content_type_field='owner_content_type', object_id_field='owner_id',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
