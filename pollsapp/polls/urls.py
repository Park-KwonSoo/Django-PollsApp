from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(template_name = 'polls/details.html'), 
    name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(template_name = 'polls/results.html'), 
    name = 'results'),
    path('<int:pk>/vote/', views.vote, name = 'vote')
]
