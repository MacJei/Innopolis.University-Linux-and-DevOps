FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano

COPY directory flaskapp.py static templates ./

RUN pip install --upgrade pip setuptools
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
CMD [ "python", "main.py"]
