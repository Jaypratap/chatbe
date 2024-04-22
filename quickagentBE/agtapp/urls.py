from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', TestAPI.as_view()),
    path('datagram/text_to_text/', TextConv.as_view()),
]