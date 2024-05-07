from django.contrib import admin
from django.urls import path, include
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', TestAPI.as_view()),
    path('datagram/text_to_text/', TextConv.as_view()),
    path('signup/', UserRegistration.as_view()),
    # path('login/', Login.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout/', UserRegistration.as_view()),
]