from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from users.models import Member
from events.choices import EVENT_VISIBILITY_CHOICES

class Event(models.Model):
    name = models.CharField(_("name"), max_length=50, null=False, blank=True)
    details = models.TextField(_("details"), default="", null=False, blank=True)
    venue = models.CharField(_("venue"), max_length=50, null=False, blank=True)
    location = models.CharField(_("location"), max_length=50, null=False, blank=True)
    visibility = models.CharField(_("visibility"), max_length=50, choices=EVENT_VISIBILITY_CHOICES, default="Public", null=False, blank=True)
    photo = models.ImageField(_("photo"), upload_to='events/%Y/%m/%d/', null=True, blank=True)
    start_time = models.DateTimeField(_("start time"), auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(_("end time"), auto_now=False, auto_now_add=False)
    owner_id = models.PositiveIntegerField(blank=True, null=False)
    owner_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    owner = GenericForeignKey(
        fk_field='owner_id',
        ct_field='owner_content_type',
    )
    #     CartItem.objects.create(
    # ...    product_content_type=ContentType.objects.get_for_model(ebook),
    # ...    product_object_id=ebook.pk,
    # ... )
    attendees = models.ManyToManyField(Member, related_name='events_attending', through='Attendee', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
