from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Question, Comment
from datetime import datetime

def home(request):
    return render(request, 'index.html')

def add_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        if question_text:
            Question.objects.create(question=question_text, timestamp=datetime.now())
            return HttpResponse('Success!')
        else: 
            return HttpResponse('Question field cannot be blank!')
    else:
        return render(request, 'index.html')
    
def get_questions(request):
    all_questions = Question.objects.all()
    questions = [
        {
            "id": question.id,
            "question": question.question,
            "timestamp": f"{question.timestamp.day}-{question.timestamp.month}-{question.timestamp.year}"
        } for question in all_questions
        
    ]
    return render(request, 'questions.html', {'questions': questions})

def question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        comments = [
            {
                "id": comment.id,
                "comment": comment.comment,
                "timestamp": comment.timestamp,
                "upvotes": comment.upvotes,
            } for comment in Comment.objects.filter(question_id=question_id).order_by('-upvotes')
        ]
        return render(request, 'question.html', {'question': {
            "id": question_id,
            "question": question.question,
            "timestamp": question.timestamp,
            "comments": comments
        }})
    except Question.DoesNotExist:
        return HttpResponse("404 Not Found")
    except Exception as e:
        return HttpResponse(e)
    
def post_comment(request, question_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(
                question = Question.objects.get(id=question_id),
                comment = comment_text,
                timestamp = datetime.now()
            )
            return redirect('question', question_id=question_id)
        else:
            return redirect('question', question_id=question_id)
    else:
        return HttpResponseRedirect('question', question_id=question_id)
    
def upvote_comment(request, question_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.increase_upvotes()
    return redirect('question', question_id=question_id)
    
