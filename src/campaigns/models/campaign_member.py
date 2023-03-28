from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.models import Member

from campaigns.choices import CAMPAIGN_ROLE_CHOICES
from .campaign import Campaign

class CampaignMember(models.Model):
    role = models.CharField(_("role"), max_length=10, default="Supporter", choices=CAMPAIGN_ROLE_CHOICES, null=False, blank=True)
    position = models.CharField(_("position"), max_length=128, null=False, blank=True)
    member = models.ForeignKey(Member, verbose_name=_("member"), on_delete=models.CASCADE, null=False, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"), on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = _("campaign member")
        verbose_name_plural = _("campaign members")
        # unique_together = (
        #     'member', 'campaign'
        # )

    def __str__(self):
        return f"{self.campaign.name}: {self.position} - {self.member.identity.name}"

    def get_absolute_url(self):
        return reverse("campaign_member_detail", kwargs={"pk": self.pk})
