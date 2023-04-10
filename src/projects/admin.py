from django.contrib import admin

from projects.models import (
    Project, 
    ProjectMember,
    Task,
    Applicant,
    Expenditure,
    Position)

admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Applicant)
admin.site.register(Expenditure)
admin.site.register(Position)
