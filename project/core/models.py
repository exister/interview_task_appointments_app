from django.db import models


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    class Meta:
        abstract = True
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    def __str__(self):
        return self.__unicode__()


class Doctor(PersonalInfo, Timestampable, models.Model):
    pass


class Patient(PersonalInfo, Timestampable, models.Model):
    pass


class Appointment(Timestampable, models.Model):
    start = models.DateTimeField()
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)

    def __unicode__(self):
        return '{} {} {}'.format(self.start, self.doctor, self.patient)
