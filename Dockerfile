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
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    #remove temp file if created while configuring
    rm -rf /tmp && \ 
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

#venv path
ENV PATH="/py/bin:$PATH"

USER django-user