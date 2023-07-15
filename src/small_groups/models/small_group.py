from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from classifications.models import Cause, Tag
from events.models import Event
from users.models import Member

class SmallGroup(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=True)
    photo = models.ImageField(_("photo"), upload_to='groups/%Y/%m/%d/', null=True, blank=True)
    about = models.TextField(_("about"), default="", null=False, blank=True)
    creator = models.ForeignKey(Member, verbose_name=_("creator"), on_delete=models.CASCADE, related_name="groups", null=False, blank=True)
    members = models.ManyToManyField(Member, related_name="small_groups", through="GroupMember", blank=True)
    events = GenericRelation(Event, content_type_field='owner_content_type', object_id_field='owner_id',)
    enabled = models.BooleanField(_("enabled"), default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("small group")
        verbose_name_plural = _("small groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
