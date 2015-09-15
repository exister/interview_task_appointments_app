import json
from django.http import HttpResponse
from django.views.generic import ListView
from ..models import Doctor


class JsonMixin(object):
    content_type = 'application/json'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return HttpResponse(
            content=json.dumps(context),
            **response_kwargs
        )


class DoctorsList(JsonMixin, ListView):
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', self.object_list)

        context = {
            'doctors': [
                {
                    'full_name': doctor.__unicode__(),
                    'id': doctor.pk
                }
                for doctor in queryset
            ]
        }
        return context

doctors_list = DoctorsList.as_view()
