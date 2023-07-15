from django.urls import include, path

from projects import views

urlpatterns = [
    path('projects/', include(([
        path('', views.project_list, name='list'),
        path('create/', views.project_create, name='create'),
        path('<int:pk>/details/', views.project_details, name='details'),
        path('<int:pk>/news/', views.project_news, name='news'),
        path('<int:pk>/goals/', views.project_goals, name='goals'),
        path('<int:pk>/events/', views.project_events, name='events'),
        path('<int:pk>/members/', views.project_members, name='members'),
        path('<int:pk>/photos/', views.project_photos, name='photos'),
        path('<int:pk>/videos/', views.project_videos, name='videos'),
        path('<int:pk>/positions/', views.project_positions, name='positions'),
        path('<int:pk>/join/', views.project_join, name='join'),
    ], 'projects'))),
]