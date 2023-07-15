from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from posts.models import Post

class Media(models.Model):
    file = models.FileField(_("media"), upload_to='posts/%Y/%m/%d/', max_length=100, null=True, blank=True)
    description = models.CharField(_("description"), max_length=100, null=False, blank=True)
    post = models.ForeignKey(Post, verbose_name=_("post"), on_delete=models.CASCADE, related_name="media", null=False, blank=True)
    
    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("media")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("media_detail", kwargs={"pk": self.pk})
