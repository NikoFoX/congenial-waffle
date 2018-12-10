from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse("Hello kind user! Here's your poll index." +
                        "Latest questions: {0}".format(output))

def detail(request, question_id):
    return HttpResponse("Here's your question: {0}.".format(question_id))

def results(request, question_id):
    return HttpResponse("Results of the question: {0}".format(question_id))

def vote(request, question_id):
    return HttpResponse("Votes of question: {0}".format(question_id))
