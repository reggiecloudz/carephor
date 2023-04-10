from django.contrib import admin

from events.models import Attendee, Event, Invitation, Schedule

admin.site.register(Attendee)
admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(Schedule)
