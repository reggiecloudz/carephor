from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from users.models import Member

from .project import Project

class Proposal(models.Model):
    problem = models.TextField(_("problem"), default="", blank=True)
    
    goal = models.TextField(_("goal"), default="", blank=True)
    
    # who
    beneficiaries = models.TextField(_("beneficiaries"), default="", blank=True)
    
    # why is the problem important
    importance = models.TextField(_("importance"), default="", blank=True)
    
    # what are you going to do to help solve the problem
    solution = models.TextField(_("solution"), default="", blank=True)
    
    # how are you going to put your solution into place
    execution = models.TextField(_("execution"), default="", blank=True)
    
    project = models.OneToOneField(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="proposal")

    class Meta:
        verbose_name = _("proposal")
        verbose_name_plural = _("proposals")

    def __str__(self):
        return f"{self.project.name} proposal"

    def get_absolute_url(self):
        return reverse("proposal_detail", kwargs={"pk": self.pk})
