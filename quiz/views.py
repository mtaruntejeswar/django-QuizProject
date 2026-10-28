from django.shortcuts import render

# Create your views here.

def teachers_dashboard(request):
    return render(request,'teachers_dashboard.html')


def create_quiz(request):
    return render(request,'create_quiz.html')

def edit_quiz(request,quiz_id):
    return render(request,'edit_quiz.html')


def view_quiz_questions(request,quiz_id):
    return render(request,'view_quiz_questions.html')


def add_question(request,quiz_id):
    return render(request,'add_question.html')

def edit_question(request,question_id):
    return render(request,'edit_question.html')

def quiz_preview(request,quiz_id):
    return render(request,'quiz_preview.html')


def publish_quiz(request):
    pass

def quiz_results(request,quiz_id):
    return render(request,'quiz_results.html')