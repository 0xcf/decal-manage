FROM python:slim-stretch

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN install -d --owner=nobody /opt/decal /opt/decal/venv
COPY requirements.txt /opt/decal
RUN python -m venv /opt/decal/venv \
    && /opt/decal/venv/bin/pip install -U pip \
    && /opt/decal/venv/bin/pip install -r /opt/decal/requirements.txt

COPY manage.py /opt/decal
COPY decaladmin /opt/decal/decaladmin/
COPY settings.conf /opt/decal

WORKDIR /opt/decal
# CMD ["/opt/decal/venv/bin/gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "decaladmin.wsgi"]
CMD ["/opt/decal/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
