from django.contrib import admin

from projects.models import (
    Project, 
    ProjectMember,
    Action,
    Applicant,
    Expenditure,
    Position,
    Proposal)

admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Action)
admin.site.register(Applicant)
admin.site.register(Expenditure)
admin.site.register(Position)
admin.site.register(Proposal)
