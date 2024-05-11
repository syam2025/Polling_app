
from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

