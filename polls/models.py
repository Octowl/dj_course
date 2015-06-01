from django.db import models


class Poll(models.Model):
    name = models.CharField("poll name", max_length=64)
    category = models.CharField("poll category", max_length=64)
    question = models.TextField(blank=True)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, verbose_name="poll question")
    label = models.CharField("answer choice", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("last updated", auto_now=True)


class Response(models.Model):
    choice = models.ForeignKey(Choice, null=True, blank=True)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
