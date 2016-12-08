FROM alpine
MAINTAINER Igor Murasev <it@chi.md>
ADD . /micro1
ENV DJANGO_SETTINGS_MODULE micro1.settings
ENV API_HOST web2
ENV DB_HOST db1
EXPOSE 8881
WORKDIR /micro1
RUN apk add --no-cache --update bash python python-dev py-pip postgresql postgresql-dev postgresql-client build-base git
RUN pip install --upgrade pip
RUN pip install -r /micro1/requirements.txt
RUN python /micro1/manage.py collectstatic --noinput
RUN mkdir -p /micro1/logs
RUN mkdir -p /micro1/public/static
CMD python /micro1/manage.py runserver 8881 >>/micro1/logs/dd.log 2>>/micro1/logs/err.log
