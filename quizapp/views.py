# -*- coding: utf-8 -*-
from django.views.generic.list_detail import object_list, object_detail
from quizapp.models import Quiz,Question,Answer
from ragendja.dbutils import get_object_or_404
import logging

def list_quiz(request):
    return  object_list(request, Quiz.all().filter('online =',True),
            paginate_by=10)

def detail_quiz(request,key):
    list_questions = get_object_or_404(Quiz,key).questions
    quiz=[]
    if list_questions!=None:
        for key_question in list_questions:
            item = {}
            answers = []
            question=get_object_or_404(Question,key_question)
            item['question']=question
            for key_answer in question.answers:
                answer=get_object_or_404(Answer,key_answer)
                answers.append(answer)
            item['answers']=answers
            quiz.append(item)
    return  object_detail(request, Quiz.all(), key,extra_context={'quiz':quiz,'result':False})

def result_quiz(request,key):
    if request.method == 'POST':
        quiz=[]
        list_questions = get_object_or_404(Quiz,key).questions
        if list_questions!=None:
            i=0
            note = 0
            for key_question in list_questions:
                i+=1
                item = {}
                answers = []
                question=get_object_or_404(Question,key_question)
                item['question']=question
                form_response = request.POST['%s' % question.key()]
                good_response = '%s' % question.question_answer.key()
                if form_response==good_response:
                    item['point']=True
                    note+=1
                else:
                    item['point']=False

                for key_answer in question.answers:
                    answer=get_object_or_404(Answer,key_answer)
                    if answer==question.question_answer:
                        answers.append(answer)
                    item['answers']=answers
                quiz.append(item)
    return  object_detail(request, Quiz.all(), key,extra_context={'quiz':quiz,'result':True,'note':note,'nbquestion':i})

