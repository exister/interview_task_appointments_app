from django.contrib import admin
from core.models import Doctor, Patient, Appointment


class DoctorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)
