import json
import datetime
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import Doctor, Appointment


class JsonMixin:
    content_type = 'application/json'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return HttpResponse(
            content=json.dumps(context),
            **response_kwargs
        )


class DoctorsList(JsonMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = {
            'doctors': [
                {
                    'full_name': doctor.__unicode__(),
                    'id': doctor.pk
                }
                for doctor in Doctor.objects.all()
            ]
        }
        return context

doctors_list = DoctorsList.as_view()


class DatesList(JsonMixin, TemplateView):
    def dates_range(self):
        today = datetime.date.today()
        i = 0
        while i < 10:
            d = today + datetime.timedelta(days=i)
            if d.weekday() < 5:
                yield d
            i += 1

    def get_context_data(self, **kwargs):
        context = {
            'dates': [
                {
                    'date': d.isoformat(),
                }
                for d in self.dates_range()
            ]
        }
        return context

dates_list = DatesList.as_view()


class TimeListForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
    date = forms.DateField(required=True)


class TimesList(JsonMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        self.form = TimeListForm(request.GET)
        if not self.form.is_valid():
            return HttpResponse(status=400)
        return super(TimesList, self).get(request, *args, **kwargs)

    def times_range(self, doctor, date):
        existing_appointments = {
            a.start: 1
            for a in Appointment.objects.filter(
                doctor=doctor,
                start__range=(
                    datetime.datetime.combine(date, datetime.time.min),
                    datetime.datetime.combine(date, datetime.time.max)
                )
            )
        }
        start = datetime.datetime.combine(date, datetime.time(9, 0, 0))
        i = 0
        while i < 9:
            d = start + datetime.timedelta(hours=i)
            if d not in existing_appointments:
                yield d
            i += 1

    def get_context_data(self, **kwargs):
        context = {
            'times': [
                {
                    'time': d.isoformat(),
                }
                for d in self.times_range(**self.form.cleaned_data)
            ]
        }
        return context

times_list = TimesList.as_view()
