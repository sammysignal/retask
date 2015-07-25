from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    email = models.EmailField(blank=True)
    email_host = models.CharField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Party(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user_host = models.ForeignKey()
    group_host = models.ForeignKey()
    invited = models.ManyToManyField(UserProfile)
    attendees = models.ManyToManyField(UserProfile)
    location = models.TextField(max_length=100)
    status = models.CharField(choices=('on', 'up', 'down', 'over'),
                              default='on')
    begin = models.DateTimeField()
    end = models.DateTimeField()
    is_private = models.BooleanField()

    def get_host(self):
        if self.user_host:
            return self.user_host
        elif self.group_host:
            return self.group_host
        else:
            raise ValueError("Host is not defined.")

    def __unicode__(self):
        return self.title
