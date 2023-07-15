from django.urls import include, path

from projects import views

urlpatterns = [
    path('project-manager/', include(([
        path('<int:pk>/', views.project_manager_about, name='about'),
        path('<int:pk>/actions/', views.project_manager_actions, name='actions'),
        path('<int:pk>/create-action/', views.action_create, name='action_create'),
        path('<int:pk>/positions/', views.project_manager_positions, name='positions'),
        path('<int:pk>/create-position/', views.position_create, name='create_position'),
        path('<int:pk>/members/', views.project_manager_members, name='members'),
        path('<int:pk>/expenditures/', views.project_manager_expenditures, name='expenditures'),
        path('<int:pk>/add-expenditure/', views.expenditure_create, name='create_expenditure'),
        path('<int:pk>/events/', views.project_manager_events, name='events'),
        path('<int:pk>/create-event/', views.project_manager_add_events, name='create_event'),
    ], 'project_managers'))),
]