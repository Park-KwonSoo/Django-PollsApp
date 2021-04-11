from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline) :
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin) :
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date Information', {
            'fields' : ['pub_date'],
            'classes' : ['collapse']    #이 코드는 Date Information을 숨기는데 사용된다.
        })
    ]
    inlines = [ChoiceInline]

    #이 코드는 전체 질문 목록을 볼 때, question 텍스트와 date, 그리고 최신 질문인지(=함수인 경우도 가능)를 표시한다.
    list_display = ('question_text', 'pub_date', 'was_published_recently')  
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)

# Register your models here.
