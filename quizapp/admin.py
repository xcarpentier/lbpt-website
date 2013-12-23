# -*- coding: latin-1 -*-
from django.contrib import admin
from quizapp.models import Quiz,Question,Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_title', 'online')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_prior', 'question_content','question_answer')
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_content',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
