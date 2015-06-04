from django.db import models
from django.conf import settings


class Poll(models.Model):

    DEMOGRAPHICS = 'DEM'
    POLITICS = 'POL'
    SPORTS = 'SPRT'
    TECHNOLOGY = 'TECH'
    ACADEMICS = 'AC'
    TRAVEL = 'TRVL'

    CATEGORY_CHOICES = (
        ('DEM', 'Demographics'),
        ('POL', 'Politics'),
        ('SPRT', 'Sports'),
        ('TECH', 'Technology'),
        ('AC', 'Academics'),
        ('TRVL', 'Travel'),
    )

    name = models.CharField("poll name", max_length=64)
    category = models.CharField("poll category",
                                choices=CATEGORY_CHOICES,
                                max_length=64)
    question = models.TextField(blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.category)

    def choice_count(self):
        return self.choice_set.count()


class Choice(models.Model):
    poll = models.ForeignKey(Poll, verbose_name="poll question")
    label = models.CharField("answer choice", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("last updated", auto_now=True)

    def __str__(self):
        return "{}".format(self.label)

    def poll_name(self):
        return self.poll.name


class Response(models.Model):
    poll = models.ForeignKey(Poll,
                             null=True, blank=True,
                             verbose_name="poll question")
    choice = models.ForeignKey(Choice, default=0)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def poll_name(self):
        return self.choice.poll.name



class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # every user has a single profile
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    location = models.CharField(max_length=64, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER)