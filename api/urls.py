from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, ProfileViewSet, RecoveryViewSet, FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('recovery', RecoveryViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'), #send me an access token
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login') #send me an access token
]
