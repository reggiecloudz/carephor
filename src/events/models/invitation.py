from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from users.models import Member
from .event import Event

class Invitation(models.Model):
    acceptance = models.BooleanField(_("acceptance"), default=False, null=False, blank=True)
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE, related_name='invitations', null=False, blank=True)
    member = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE, related_name='invitations', null=False, blank=True)
    message = models.TextField(_("message"), default="", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("invitation")
        verbose_name_plural = _("invitations")

    def __str__(self):
        return f"{self.member.identity.name} invitation to {self.event.name}"

    def get_absolute_url(self):
        return reverse("invitation_detail", kwargs={"pk": self.pk})
