from django.urls import include, path

from posts import views

urlpatterns = [
    path('posts/', include(([
        path('<int:pk>/', views.post_photo_create, name='photo_create'),
    ], 'posts')))
]