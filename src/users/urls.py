from django.urls import include, path

from users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('', include(([
        path('user/registration/', views.register_user, name='signup'),
    ], 'registration'))),
    path('members/', include(([
        path('<int:pk>/', views.member_detail, name='member_detail'),
    ], 'members'))),
]