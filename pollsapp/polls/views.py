from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

from .models import Question, Choice

def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

def details(request, question_id) :
    try : 
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist :
        raise Http404("Question Does not exist")
    return render(request, 'polls/details.html', {'question' : question})

def results(request, question_id) :
    detail_question = Question.objects.get(pk = question_id)
    vote_results = '\n'.join([{c.choice_text : str(c.votes)} for c in detail_question.choice_set.all()])
    return HttpResponse(vote_results)

def vote(request, question_id) :
    question = Question.objects.get(pk = question_id)
    print(request.hi)
    return HttpResponse(question)
# Create your views here.
