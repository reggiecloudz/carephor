from django.urls import include, path

from small_groups import views

urlpatterns = [
    path('groups/', include(([
        # path('', cause_collection, name='cause_collection'),
        path('<int:pk>/', views.group_details, name='details'),
        path('<int:pk>/events/', views.group_events, name='events'),
        path('<int:pk>/members/', views.group_members, name='members'),
    ], 'groups')))
]