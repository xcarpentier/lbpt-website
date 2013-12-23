# -*- coding: latin-1 -*-
from google.appengine.ext import db
from ragendja.dbutils import KeyListProperty
from core.models import HTMLProperty

class Answer(db.Model):
    answer_content = db.StringProperty(required=True,verbose_name=u"R�ponse")
    def __unicode__(self):
        return u'R�ponse : %s' % (self.answer_content)
    
    class Meta:
        verbose_name = u'R�ponse'
        verbose_name_plural = u'R�ponses'

class Question(db.Model):
    question_prior = db.IntegerProperty(required=True,verbose_name=u"Num�ro")
    question_content = db.TextProperty(required=True,verbose_name="Question")
    answers = KeyListProperty(Answer,verbose_name=u"R�ponse")
    question_answer = db.ReferenceProperty(Answer,verbose_name=u"Bonne r�ponse")
    def __unicode__(self):
        return u'Question : %s - %s' % (self.question_prior,self.question_content)
        
class Quiz(db.Model):
    quiz_title = db.StringProperty(required=True,verbose_name="Titre")
    quiz_description = HTMLProperty(required=True,verbose_name="Description")
    online = db.BooleanProperty(required=True,verbose_name="En ligne")
    questions = KeyListProperty(Question)
    def __unicode__(self):
        return u'Quiz : %s' % (self.quiz_title)