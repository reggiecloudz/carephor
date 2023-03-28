from django.urls import include, path

from campaigns.views import (
    campaign_details, 
    campaign_news, 
    campaign_events, 
    campaign_members,
    campaign_positions,
    campaign_photos,
    campaign_videos)

urlpatterns = [
    path('campaigns/', include(([
        path('<int:pk>/', campaign_details, name='details'),
        path('<int:pk>/news/', campaign_news, name='news'),
        path('<int:pk>/events/', campaign_events, name='events'),
        path('<int:pk>/members/', campaign_members, name='members'),
        path('<int:pk>/positions/', campaign_positions, name='positions'),
        path('<int:pk>/photos/', campaign_photos, name='photos'),
        path('<int:pk>/videos/', campaign_videos, name='videos'),
    ], 'campaigns'))),
]