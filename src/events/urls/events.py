from django.urls import include, path

from events import views

urlpatterns = [
    path('events/', include(([
        path('<int:pk>/', views.event_details, name='details'),
        path('<int:pk>/info/', views.event_info, name='info'),
    ], 'events'))),
]