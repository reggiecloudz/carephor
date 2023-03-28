from django.urls import include, path

# from campaigns.apis import cause_collection, cause_single

urlpatterns = [
    path('api/v1/causes/', include(([
        # path('', cause_collection, name='cause_collection'),
        # path('<int:pk>/', cause_single, name='cause_single'),
    ], 'causes-api')))
]