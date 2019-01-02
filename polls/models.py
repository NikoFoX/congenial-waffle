import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, help_text="Text of the choice")
    votes = models.IntegerField(default=0)
    #choice_rank = models.IntegerField(default=0)

    def Choice(self, text):
        choice_text = str(text)

    def _int_(self):
        return self.choice_text

    def __str__(self):
        return self.choice_text
