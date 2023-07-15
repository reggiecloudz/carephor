from django.urls import include, path

from small_groups import views

urlpatterns = [
    path('groups/', include(([
        path('<str:slug>/', views.group_profile, name='profile'),
        path('<int:pk>/details/', views.group_details, name='details'),
        path('<int:pk>/events/', views.group_events, name='events'),
        path('<int:pk>/members/', views.group_members, name='members'),
        path('<int:pk>/join/', views.group_join, name='join'),
    ], 'groups')))
]