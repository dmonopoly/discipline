from django.db import models


class User(models.Model):
  name = models.CharField(max_length=25)
  ip_address = models.CharField(max_length=25)
  focusing = models.BooleanField(default=False)
  last_pass_time = models.DateTimeField()

  def __unicode__(self):
    return "User " + str(self.ip_address) + ", focusing=" + str(self.focusing) + \
        "\tLast entry/exit: " + str(self.last_pass_time)

class Block(models.Model):
  user = models.ForeignKey(User)

  def __unicode__(self):
    return "Block for \n" + str(self.user)

