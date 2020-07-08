from django.urls import path,include
# from api.views import registration_view
from api.views import  NameRegistrationView,FacebookLogin
from api.views import GoogleLogin


app_name='Payu'

urlpatterns = [
    # path('reg', registration_view), 
    path('api/', include('rest_auth.urls')), 
    path('api/register/', NameRegistrationView.as_view(), name="rest_name_register"),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='goggle_login')


]
