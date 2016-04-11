
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("OMDERMAN",max_length=200)
    your_name = models.CharField(max_length=200)
    your_age = models.CharField(max_length=200,default='mohamed wdalnor')
    pub_date = models.DateTimeField('published on ')
    your_name.blank=True
    sudan = 'SD'
    qatar = 'QR'
    usa = 'US'
    country = (
        (sudan, 'Sudan'),
        (qatar, 'Qatar'),
        (usa, 'Usa'),
    )
    mycountry = models.CharField(max_length=2,choices=country,default=usa)

    def is_upperclass(self):
        return self.mycountry in (self.Usa, self.Qatar)
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 
    def __str__(self):
        return self.choice_text

