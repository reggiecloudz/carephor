from django.urls import path, include

urlpatterns = [
    path('', include('campaigns.urls.campaigns')),
    # path('', include('campaigns.urls.causes')),
]