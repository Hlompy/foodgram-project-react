from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, UserSignupViewSet, UserJSWTokenViewSet,
                    FollowListView, FollowViewSet)

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('auth/signup', UserSignupViewSet)
router_v1.register('auth/token', UserJSWTokenViewSet)

urlpatterns = [
    path(
        'users/subscriptions/',
        FollowListView.as_view(),
        name='subscriptions'
    ),
    path(
        'users/<int:user_id>/subscribe/',
        FollowViewSet.as_view(),
        name='subscribe'
    ),
    path('v1/', include(router_v1.urls)),
]
