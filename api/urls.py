from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, ProfileViewSet,AddLoanViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('loan/add', AddLoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
