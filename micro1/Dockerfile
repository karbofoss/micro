FROM python:2.7
MAINTAINER Igor Murasev <it@chi.md>
ADD . /micro1
ENV DJANGO_SETTINGS_MODULE micro1.settings
ENV API_HOST web2
ENV DB_HOST db1
EXPOSE 8881
WORKDIR /micro1
RUN apt-get update
RUN apt-get install -y postgresql-client
RUN pip install -r /micro1/requirements.txt
RUN python /micro1/manage.py collectstatic --noinput
RUN mkdir /micro1/logs
CMD python /micro1/manage.py runserver 8881 >>/micro1/logs/dd.log 2>>/micro1/logs/err.log
