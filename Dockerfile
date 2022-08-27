FROM  python:3.9-alpine3.13
LABEL maintainer = "Lord_mi_mi"
ENV PYTHONUNBUFFERED 1
COPY . /DOG-DOG
WORKDIR /DOG-DOG/
EXPOSE 8000
RUN pip install  --upgrade pip && \
    apk add --update --no-cache postgresql-client build-base postgresql-dev musl-dev  zlib-dev jpeg-dev && \
    pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user
WORKDIR /DOG-DOG/good_heartst_project
CMD python manage.py runserver