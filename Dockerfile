FROM python:3.9-alpine3.13
#whos maitaining
LABEL maintainer="Ashwin Patil"
#Console python print 
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
# Commands executed from
WORKDIR /app
EXPOSE 8000

# this can be overrided in Docker Compose file
ARG DEV=false
#avoid multiple docker image layer for dependencies as added, single one
# apk used in alpine version of linux to add package
RUN python -m venv /py && \
    apk add --update --no-cache postgresql-client && \
    # add the dependencies to be installed location, tmp dependencies added for making posgres interact
    apk add --update --no-cache --virtual .tmp-build-deps \
    # add the dependencies(libraries) required for interacting in virtual loaction provided, develop the dependencies
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    #remove temp file if created while configuring
    rm -rf /tmp && \ 
    # remove the dependencies added, grouped so that it can be removed easily
    apk del .tmp-build-deps && \ 
    # /var/cache/apk/ this location has packages necessary only
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

#venv path
ENV PATH="/py/bin:$PATH"

USER django-user