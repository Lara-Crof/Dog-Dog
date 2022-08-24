FROM  python:3.9-alpine3.13
LABEL maintainer = "Lord_mi_mi"

ENV PYTHONUNBUFFERED 1

COPY . /DOG-DOG



EXPOSE 8000

RUN pip install  --upgrade pip && \
apk add --update --no-cache postgresql-client && \
apk add --update --no-cache --virtual .tmp-build-deps\
    build-base postgresql-dev musl-dev  zlib-dev jpeg-dev  && \
pip install -r /DOG-DOG/requirements.txt && \
apk del .tmp-build-deps && \
adduser \
--disabled-password \
--no-create-home  \
django-user
WORKDIR /DOG-DOG/good_heartst_project
CMD python3 manage.py runserver 