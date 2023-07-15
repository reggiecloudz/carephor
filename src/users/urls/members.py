from django.urls import include, path

from users import views

urlpatterns = [
    # path('assignments/<int:action_pk>/', views.member_assignment_details, name='assignment'),
    path('members/', include(([
        path('<int:pk>/', views.member_detail, name='details'),
        path('<int:pk>/calendar/', views.member_calendar, name='calendar'),
        path('<int:pk>/applications/', views.member_applications, name='applications'),
        path('<int:pk>/projects/', views.member_projects, name='projects'),
        path('<int:pk>/groups/', views.member_groups, name='groups'),
        path('<int:pk>/group-create/', views.member_group_create, name='group_create'),
    ], 'members'))),
]