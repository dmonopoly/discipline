from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
  user = models.OneToOneField(User)
  ip_address = models.CharField(max_length=25)
  focusing = models.BooleanField(default=False)
#   last_pass_time = models.DateTimeField()

  def __unicode__(self):
    return "%s | IP: %s | Focusing: %s" % (self.user.username,
        self.ip_address, self.focusing)

class Category(models.Model):
  name = models.CharField(max_length=25)

  def __unicode__(self):
    return self.name

class Block(models.Model):
  person = models.ForeignKey(MyUser)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  category = models.ForeignKey(Category)

  def __unicode__(self):
    return "Person %s | %s-%s | %s \n" % (self.person, self.start_time,
        self.end_time, self.category)
