from django.urls import include, path

from projects import views

urlpatterns = [
    path('positions/', include(([
        path('<int:pk>/', views.position_details, name='details'),
    ], 'positions'))),
]