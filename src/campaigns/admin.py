from django.contrib import admin

from campaigns.models import (
    Campaign, 
    CampaignMember, 
    Cause,
    Action,
    Applicant,
    Expenditure,
    Goal,
    Position)

admin.site.register(Cause)
admin.site.register(Campaign)
admin.site.register(CampaignMember)
admin.site.register(Action)
admin.site.register(Applicant)
admin.site.register(Expenditure)
admin.site.register(Goal)
admin.site.register(Position)
