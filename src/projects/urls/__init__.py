from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls.projects')),
    path('', include('projects.urls.project_managers')),
    path('', include('projects.urls.positions')),
    path('', include('projects.urls.actions')),
]