from datetime import date, timedelta
from django import template
from eventapp.models import Agenda
import logging
register = template.Library()

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

@register.inclusion_tag('eventapp/month_cal.html')
def month_cal():
    year = date.today().year
    month = date.today().month
    
    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())

    month_cal = []
    week = []
    week_headers = []
    today = date.today()

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        for event in Agenda.all().filter('agenda_online = ',True):
            if day >= event.agenda_startdate.date() and day <= event.agenda_enddate.date():
                cal_day['event'] = True
                cal_day['title'] = event.title_event
                cal_day['key'] = event.key()
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False  
        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)
        before = date.today().month - 1
        next = date.today().month + 1

    return {'calendar': month_cal, 'headers': week_headers, 'today' : today, 'before':before, 'next':next}