from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.choices import *

class Member(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    about = models.TextField(_("about"), default="", blank=True)
    cover_photo = models.ImageField(_("cover photo"), upload_to='members/%Y/%m/%d/', null=True, blank=True)
    occupation = models.CharField(_("occupation"), max_length=255, default="Not Provided", null=False, blank=True)
    education = models.CharField(
        _("education"), 
        max_length=75, 
        choices=EDUCATION, 
        default="Not Specified", 
        blank=True
    )
    denomination = models.CharField(
        _("denomination"), 
        max_length=75, 
        choices=DENOMINATION_CHOICES, 
        default='Theist',
        blank=True
    )
    interests = models.JSONField(_("interests"), default=list, null=True, blank=True)
    values = models.JSONField(_("values"), default=list, null=True, blank=True)
    identity = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("identity"), on_delete=models.CASCADE, related_name="member", null=False, blank=True)
    connection_requests = models.ManyToManyField("self", verbose_name=_("connection requests"), through="ConnectionRequest", blank=True)
    connections = models.ManyToManyField("self", verbose_name=_("connections"), through="Connection", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")

    def __str__(self):
        return self.identity.username

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.identity.username)
        return super().save(*args, **kwargs)