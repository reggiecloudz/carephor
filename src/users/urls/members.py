from django.urls import include, path

from users import views

urlpatterns = [
    path('members/', include(([
        path('<int:pk>/', views.member_detail, name='detail'),
        path('<int:pk>/applications/', views.member_applications, name='applications'),
        path('<int:pk>/projects/', views.member_projects, name='projects'),
        path('<int:pk>/groups/', views.member_groups, name='groups'),
    ], 'members'))),
]