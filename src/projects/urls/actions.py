from django.urls import include, path

from projects import views

urlpatterns = [
    path('actions/', include(([
        path('<int:pk>/details/', views.action_detail, name='details'),
        path('<int:pk>/update/', views.action_update, name='update'),
        path('<int:pk>/assign/', views.action_assign, name='assign'),
        path('<int:pk>/delete/', views.action_delete, name='delete'),
        path('<int:pk>/start/', views.action_start, name='start'),
        path('<int:pk>/complete/', views.action_complete, name='complete'),
    ], 'actions'))),
]