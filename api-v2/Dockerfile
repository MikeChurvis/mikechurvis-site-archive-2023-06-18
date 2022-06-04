FROM python:3-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /portfolio

COPY requirements.txt .

# psycopg2 isn't building as expected. I'm switching to psycopg2-binary for the sake of time.
# I'll come back to this later.

#RUN apt-get update &&\
#    BUILD_DEPENDENCIES="build-essential libpcre3-dev libpq-dev" &&\
#    apt-get install -y --no-install-recommends $BUILD_DEPENDENCIES &&\
#    pip install --no-cache-dir virtualenv &&\
#    python -m virtualenv venv &&\
#    . ./venv/bin/activate &&\
#    pip install --no-cache-dir --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt &&\
#    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPENDENCIES &&\
#    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir virtualenv &&\
    python -m virtualenv venv &&\
    . ./venv/bin/activate &&\
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Mark entrypoint as executable.
RUN ["chmod", "+x", "/portfolio/entrypoint.sh"]
ENTRYPOINT ["/portfolio/entrypoint.sh"]