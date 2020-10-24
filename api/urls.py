from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, ProfileViewSet, RecoveryViewSet, LoanViewSet, DeleteAccount, PaymentViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('recovery', RecoveryViewSet)
router.register('loan', LoanViewSet)
router.register('delete/account', DeleteAccount)
router.register('payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
