from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    subject = models.CharField(verbose_name='Website',max_length=200)
    description = models.TextField(verbose_name='Comments')
    publication_date = models.DateTimeField()
    visit = models.IntegerField(verbose_name='My Visits',default=0)
    cmpnyvisit = models.IntegerField(verbose_name='Currently Browsed By',default=100)
    def __unicode__(self):
        return self.subject
    def published_today(self):
        return self.publication_date.date() == timezone.now().date()
        # return self.publication_date.date() == datetime.date.today()
    published_today.boolean = True
    published_today.short_description = 'Asked today?'
    publication_date = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField()
    best_answer = models.BooleanField("preferred answer",default=False)
    def __unicode__(self):
        return self.content