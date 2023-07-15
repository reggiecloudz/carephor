from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from small_groups.models import SmallGroup
from users.models import Member

class Poll(models.Model):
    question = models.CharField(_("question"), max_length=255, null=False, blank=True)
    expiration = models.DateField(_("expiration date"), auto_now=False, auto_now_add=False)
    open = models.BooleanField(_("open status"), default=False, blank=True)
    publish = models.BooleanField(_("published status"), default=False, blank=True)
    group = models.ForeignKey(SmallGroup, verbose_name=_("group"), related_name="polls", on_delete=models.CASCADE, null=False, blank=True)
    creator = models.ForeignKey(Member, verbose_name=_("creator"), on_delete=models.CASCADE, related_name="polls", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("poll")
        verbose_name_plural = _("polls")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("poll_detail", kwargs={"pk": self.pk})

class Choice(models.Model):
    text = models.CharField(_("text"), max_length=255, null=False, blank=True)
    poll = models.ForeignKey(Poll, verbose_name=_("poll"), on_delete=models.CASCADE, related_name="choices")

    class Meta:
        verbose_name = _("choice")
        verbose_name_plural = _("choices")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("choice_detail", kwargs={"pk": self.pk})

class ChoiceVoteCount(models.Model):
    votes = models.PositiveIntegerField(_("votes"), default=0, null=False, blank=True)
    choice = models.ForeignKey(Choice, verbose_name=_("choice"), on_delete=models.CASCADE, related_name="choice_votes", null=False, blank=True)
    voter = models.CharField(_("voter"), max_length=144, unique=True, null=False, blank=True)
    
    class Meta:
        verbose_name = _("choice vote count")
        verbose_name_plural = _("choice vote counts")
        unique_together = (
            'choice', 'voter'
        )

    def __str__(self):
        return f"{self.choice.text}"

    def get_absolute_url(self):
        return reverse("choice_vote_count_detail", kwargs={"pk": self.pk})
