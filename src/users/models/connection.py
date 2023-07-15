from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.choices import CONNECTION_REQUEST_CHOICES
from .member import Member

class ConnectionRequest(models.Model):
    status = models.CharField(_("status"), max_length=50, choices=CONNECTION_REQUEST_CHOICES, default="Pending", null=True, blank=False)
    receiver = models.ForeignKey(Member, verbose_name=_("receiver"), on_delete=models.CASCADE, related_name="received_requests")
    sender = models.ForeignKey(Member, verbose_name=_("sender"), on_delete=models.CASCADE, related_name="sent_requests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("connection request")
        verbose_name_plural = _("connection requests")

    def __str__(self):
        return f"{self.sender.identity.name} request for {self.receiver.identity.name}"

    def get_absolute_url(self):
        return reverse("connection_request_details", kwargs={"pk": self.pk})

class Connection(models.Model):
    sender = models.ForeignKey(Member, verbose_name=_("sender"), on_delete=models.CASCADE, related_name="sender_connections")
    receiver = models.ForeignKey(Member, verbose_name=_("receiver"), on_delete=models.CASCADE, related_name="receiver_connections")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("connection")
        verbose_name_plural = _("connections")

    def __str__(self):
        return f"{self.sender.identity.name} for {self.receiver.identity.name}"

    def get_absolute_url(self):
        return reverse("connection_details", kwargs={"pk": self.pk})