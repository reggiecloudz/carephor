from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Group(models.Model):
    name = models.CharField(_("name"), max_length=50, null=False, blank=True)
    photo = models.ImageField(_("photo"), upload_to='groups/%Y/%m/%d/', null=True, blank=True)
    about = models.TextField(_("about"), default="", null=False, blank=True)
    
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"pk": self.pk})
