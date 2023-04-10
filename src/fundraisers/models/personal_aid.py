from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member

class PersonalAid(models.Model):
    title = models.CharField(_("title"), max_length=100, null=False, blank=True)
    details = models.TextField(_("details"), null=False, blank=True)
    creator = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE, related_name="personal_aid", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("personal aid")
        verbose_name_plural = _("personal aids")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("personal_aid_detail", kwargs={"pk": self.pk})
