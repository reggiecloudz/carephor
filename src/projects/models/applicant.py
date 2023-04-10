from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from users.models import Member

from .position import Position

class Applicant(models.Model):
    selected = models.BooleanField(_("selected"), default=False, blank=True)
    qualifications = models.TextField(_("qualifications"), null=True, blank=True)
    member = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE, related_name="applications", null=False, blank=True)
    position = models.ForeignKey(Position, verbose_name=_("position"), on_delete=models.CASCADE, related_name="applicants", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("applicant")
        verbose_name_plural = _("applicants")

    def __str__(self):
        return f"{self.position.title}: {self.member.identity.name}"

    def get_absolute_url(self):
        return reverse("applicant_detail", kwargs={"pk": self.pk})
