from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MyUser(models.Model):
  user = models.OneToOneField(User)
  username = models.CharField(max_length=25)
  ip_address = models.CharField(max_length=25)
  focusing = models.BooleanField(default=False)
  start_time = models.DateTimeField()

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

class Site(models.Model):
  url = models.CharField(max_length=1000, blank=True)
  hostname = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=timezone.now())
  visits = models.IntegerField(default=0)
  name = models.CharField(max_length=20)

  def __unicode__(self):
    return self.hostname + ", " + self.url
