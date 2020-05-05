from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from fullcalendar.models import CalendarEvent
from fullcalendar.util import events_to_json, calendar_options
from django.contrib import messages
from .forms import BookingForm


# This is just an example for this demo. You may get this value
# from a separate file or anywhere you want

OPTIONS = """{  timeFormat: "H:mm",
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay',
                },
                allDaySlot: false,
                firstDay: 0,
                weekMode: 'liquid',
                slotMinutes: 15,
                defaultEventMinutes: 30,
                minTime: 8,
                maxTime: 20,
                editable: false,
                dayClick: function(date, allDay, jsEvent, view) {
                    if (allDay) {       
                        $('#calendar').fullCalendar('gotoDate', date)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
                eventClick: function(event, jsEvent, view) {
                    if (view.name == 'month') {     
                        $('#calendar').fullCalendar('gotoDate', event.start)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
            }"""

def index(request):    
    event_url = 'all_events/'
    return render(request, 'index.html', {'calendar_config_options': calendar_options(event_url, OPTIONS)})

def all_events(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')

def book(request):
    form = BookingForm(request.POST or None)

    if form.is_valid():
        data = request.POST.copy()
        if len(CalendarEvent.objects.all().filter(room=data.get('room')).filter(start__lte=data.get('start')).filter(end__gte=data.get('end'))) > 0:
            messages.error(request, "Dates Already Booked")
        else:
            form.save()
  
    form = BookingForm()
    context = {'form': form }
    return render(request, 'add_event.html', context)
