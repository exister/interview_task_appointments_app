import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import CreateView
from ..models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    middle_name = forms.CharField(max_length=255, required=True)
    start = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = Appointment
        fields = ('start', 'doctor', 'first_name', 'last_name', 'middle_name')

    def clean(self):
        cleaned_data = super().clean()

        patient, created = Patient.objects.get_or_create(
            first_name=cleaned_data.get('first_name'),
            last_name=cleaned_data.get('last_name'),
            middle_name=cleaned_data.get('middle_name'),
        )
        self.instance.patient = patient

        if Appointment.objects.filter(
            doctor=cleaned_data.get('doctor'),
            start=cleaned_data.get('start')
        ).exists():
            raise ValidationError('This time is taken')

        return cleaned_data


class IndexPage(CreateView):
    template_name = 'core/index.html'
    form_class = AppointmentForm
    success_url = '/'

index_page = IndexPage.as_view()
