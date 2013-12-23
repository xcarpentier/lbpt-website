# -*- coding: latin-1 -*-
from google.appengine.ext import db
from ragendja.dbutils import KeyListProperty
from core.models import HTMLProperty

class Answer(db.Model):
    answer_content = db.StringProperty(required=True,verbose_name=u"Réponse")
    def __unicode__(self):
        return u'Réponse : %s' % (self.answer_content)
    
    class Meta:
        verbose_name = u'Réponse'
        verbose_name_plural = u'Réponses'

class Question(db.Model):
    question_prior = db.IntegerProperty(required=True,verbose_name=u"Numéro")
    question_content = db.TextProperty(required=True,verbose_name="Question")
    answers = KeyListProperty(Answer,verbose_name=u"Réponse")
    question_answer = db.ReferenceProperty(Answer,verbose_name=u"Bonne réponse")
    def __unicode__(self):
        return u'Question : %s - %s' % (self.question_prior,self.question_content)
        
class Quiz(db.Model):
    quiz_title = db.StringProperty(required=True,verbose_name="Titre")
    quiz_description = HTMLProperty(required=True,verbose_name="Description")
    online = db.BooleanProperty(required=True,verbose_name="En ligne")
    questions = KeyListProperty(Question)
    def __unicode__(self):
        return u'Quiz : %s' % (self.quiz_title)