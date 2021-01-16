from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from authentication.views import RegistrationView, LogoutView, AboutMeView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', AboutMeView.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
