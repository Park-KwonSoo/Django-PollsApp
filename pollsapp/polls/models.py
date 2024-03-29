import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model) :
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
    # __str__ :클래스 자체의 내용을 리턴하는 메소드 
    def __str__(self) : 
        return self.question_text

    # 최근에 발행된 Question들을 리턴한다.
    def was_published_recently(self) :
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    
    was_published_recently.short_description = "Published Recently?"
    was_published_recently.admin_order_field = "pub_date"

class Choice(models.Model) : 
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self) :
        return self.choice_text
# Create your models here.
