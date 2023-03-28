from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from users.models import Member

from .cause import Cause

class Campaign(models.Model):
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    name = models.CharField(_("name"), max_length=128, null=False, blank=True)
    overview = models.TextField(_("overview"), default="", null=False, blank=True)
    vision = models.TextField(_("vision"), default="", null=False, blank=True)
    beneficiaries = models.JSONField(_("beneficiaries"), default=list, null=True, blank=True)
    photo = models.ImageField(upload_to='campaigns/%Y/%m/%d/', null=True, blank=True)
    financial_goal = models.DecimalField(_("financial goal"), max_digits=11, decimal_places=2, null=True, blank=True)
    funds_raised = models.DecimalField(_("funds raised"), default=0, max_digits=11, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    manager = models.ForeignKey(Member, verbose_name=_("manager"), on_delete=models.CASCADE, related_name="campaigns_managed", null=False, blank=True)
    cause = models.ForeignKey(Cause, verbose_name=_("cause"), on_delete=models.CASCADE, related_name="campaigns", null=False, blank=True)
    members = models.ManyToManyField(Member, related_name="campaigns", through="CampaignMember", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("campaign")
        verbose_name_plural = _("campaigns")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("campaign_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
