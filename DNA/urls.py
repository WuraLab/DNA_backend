
from django.contrib import admin
from django.urls import  path
from django.conf.urls import  include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import  FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<version>/', include('api.urls')),
    path('api/login/', obtain_auth_token),
    path('api/<version>/rest-auth/', include('rest_auth.urls')),
    path('api/<version>/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/<version>/rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
