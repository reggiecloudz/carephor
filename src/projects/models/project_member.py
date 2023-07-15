from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member

from projects.choices import PROJECT_ROLE_CHOICES
from .project import Project

class ProjectMember(models.Model):
    role = models.CharField(_("role"), max_length=10, default="Supporter", choices=PROJECT_ROLE_CHOICES, null=False, blank=True)
    position = models.CharField(_("position"), max_length=128, null=False, blank=True)
    member = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE, null=False, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = _("project member")
        verbose_name_plural = _("project members")
        # unique_together = (
        #     'member', 'project'
        # )

    def __str__(self):
        return f"{self.project.name}: {self.position} - {self.member.identity.name}"

    def get_absolute_url(self):
        return reverse("project_member_detail", kwargs={"pk": self.pk})

    def get_members_by_role(self, role):
        members = []