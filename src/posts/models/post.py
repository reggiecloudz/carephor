from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from small_groups.models import SmallGroup
from users.models import Member

POST_TYPE_CHOICES = (
    ('Text', 'Text'), # { body }
    ('Photo', 'Photo'), # { caption, source_url }
    ('Video', 'Video'), # { description, source_url }
)

class Post(models.Model):
    author = models.ForeignKey(Member, related_name='posts', on_delete=models.CASCADE, null=False, blank=True)
    post_type = models.CharField(
        _("post type"), 
        max_length=20, 
        choices=POST_TYPE_CHOICES, 
        default="Text", 
        blank=True
    )
    text = models.TextField(_("text"), blank=True)
    group = models.ForeignKey(SmallGroup, verbose_name=_("group"), related_name="posts", on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return f"{self.author.slug} posted for {self.group.name} on {self.created_at}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
