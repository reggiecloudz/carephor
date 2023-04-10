from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member

from .small_group import SmallGroup

class GroupMember(models.Model):
    member = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE)
    small_group = models.ForeignKey(SmallGroup, verbose_name=_("small group"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("group member")
        verbose_name_plural = _("group members")

    def __str__(self):
        return f"{self.member.identity.name} in {self.small_group.name}"

    def get_absolute_url(self):
        return reverse("group_member_detail", kwargs={"pk": self.pk})
