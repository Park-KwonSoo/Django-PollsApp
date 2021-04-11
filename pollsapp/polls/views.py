from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone

from reportlab.pdfgen import canvas
from .models import Question, Choice

# def index(request) :
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html', {
#         'latest_question_list' : latest_question_list
#     })
class IndexView(ListView) :
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'
    
    def get_queryset(self) :
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5] #pub_date__lte : pub_date의 최댓값, 즉 pub_date가 now보다 작거나 같은 애들


# def details(request, question_id) :
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/details.html', {
#         'question' : question
#     })
class DetailView(DetailView) :
    def get_queryset(self) :
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        );
    

# def results(request, question_id) :
#     question = Question.objects.get(pk = question_id)
#     return render(request, 'polls/results.html', {
#         'question' : question
#     })
class ResultsView(DetailView) :
    def get_queryset(self) :
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        );
 

def vote(request, pk) :
    question = get_object_or_404(Question, pk = pk)
    try :
        selected_choice = question.choice_set.get(pk = int(request.POST['choice']))
    except (KeyError, Choice.DoesNotExist) :
        return render(request, 'polls/details.html', {
            'question' : question,
            'error_message' : "You didn't select a Choice."
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()

        pdf_file = canvas.Canvas("result_" + str(timezone.now()) + ".pdf")
        
        for ch in question.choice_set.all() :
            pdf_file.drawString(300, 300, str(ch.choice_text) + "\t" + str(ch.votes))

        pdf_file.save()

        return HttpResponseRedirect(reverse('polls:results', args = [pk]))