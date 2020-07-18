from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/login/', obtain_auth_token), # Authenticate the login credentials and return the AuthToken

]
