FROM python:2.7
MAINTAINER Igor Murasev <it@chi.md>
ADD . /micro2
ENV DJANGO_SETTINGS_MODULE micro2.settings
ENV DB_HOST db2
EXPOSE 8882
WORKDIR /micro2
RUN apt-get update
RUN apt-get install -y postgresql-client
RUN pip install -r /micro2/requirements.txt
RUN python /micro2/manage.py collectstatic --noinput
RUN mkdir -p /micro2/logs
RUN mkdir -p /micro2/public/static
CMD python /micro2/manage.py runserver 8882 >>/micro2/logs/dd.log 2>>/micro2/logs/err.log
