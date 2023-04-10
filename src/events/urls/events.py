from django.urls import include, path

from events import views

urlpatterns = [
    path('events/', include(([
        path('<int:pk>/', views.event_details, name='details'),
    ], 'events'))),
]