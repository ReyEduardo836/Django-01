from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    #Trae todas las preguntas de la base de datos
    latest_question_list = Question.objects.all() 
    
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    #trae todas las opciones de respuesta de la pregunta seleccionada
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero {question_id}")