from django.urls import include, path

from projects import views

urlpatterns = [
    path('positions/', include(([
        path('<int:pk>/', views.position_details, name='details'),
        path('<int:pk>/apply/', views.position_apply, name='apply'),
        path('<int:pk>/applicants/', views.position_applicants, name='applicants'),
        path('<int:pk>/select-applicant/', views.position_select_applicant, name='select_applicant'),
    ], 'positions'))),
]