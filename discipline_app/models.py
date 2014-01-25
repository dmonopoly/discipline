from django.db import models


class User(models.Model):
  ip_address = models.CharField(max_length=25)
  focusing = models.BooleanField()

  def __unicode__(self):
    return "User " + str(ip_address) + ", focusing=" + str(focusing)

