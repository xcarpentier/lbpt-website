# -*- coding: latin-1 -*-
from django import forms

class SubscribeForm(forms.Form):
    first_name = forms.RegexField(regex=r'^\w+$', max_length=30,label=u'Prénom',required=True)
    last_name = forms.RegexField(regex=r'^\w+$', max_length=30,label=u'Nom',required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),label=u'Adresse email',required=True)
    type_email=forms.ChoiceField(choices = ((u"HTML", u"Html"), (u"TEXT", u"Text brut")))
    