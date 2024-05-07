from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date

from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
  email = models.EmailField(_('email address'), unique = True)
  phone_no = models.CharField(max_length = 10)
  def __str__(self):
      return "{}".format(self.email)

  def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

class InteractionUser(models.Model):
    user_id = models.IntegerField()
    session_id = models.IntegerField()
    conv_start_time = models.DateTimeField()
    conv_end_time = models.DateTimeField()


class InteractionUser(models.Model):
    session_id = models.IntegerField()
    conv_data = models.CharField(max_length = 1024)
    conv_time = models.DateTimeField()

