FROM base/djangoapp_project:latest
MAINTAINER Mikhail Kuznetsov <mkuznetsov.dev@gmail.com>

ADD . /app
RUN pip3 install -r /app/requirements/production.txt
ENV DJANGO_SETTINGS_MODULE project.settings.production
ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

WORKDIR /app
EXPOSE 8000
CMD ["/usr/bin/uwsgi", "--plugin=python", "--ini", "/app/uwsgi.ini"]