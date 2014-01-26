from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
  user = models.OneToOneField(User)
  ip_address = models.CharField(max_length=25)
  focusing = models.BooleanField(default=False)
#   last_pass_time = models.DateTimeField()

  def __unicode__(self):
    return "User %s | IP: %s | Focusing: %s" % (self.user.username,
        self.ip_address, self.focusing)

class Block(models.Model):
  person = models.ForeignKey(MyUser)

  def __unicode__(self):
    return "Block for \n" + str(self.person)

