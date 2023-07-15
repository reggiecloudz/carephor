from django.urls import include, path

from users import views

urlpatterns = [
    path('profiles/', include(([
        path('', views.profile_list, name='list'),
        path('<str:slug>/', views.profile, name='profile'),
        path('<str:slug>/about/', views.profile_about, name='about'),
    ], 'profiles'))),
]