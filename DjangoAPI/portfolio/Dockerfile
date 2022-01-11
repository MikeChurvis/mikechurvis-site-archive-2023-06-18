# Alpine still is still very slow and doesn't support wheels.
FROM python:3.9-slim

WORKDIR /usr/src/app

# Process is run once per container instance; 
# saving the bytecode has no benefit.
# Source: https://stackoverflow.com/a/60797635/11294744
ENV PYTHONDONTWRITEBYTECODE 1

# Realtime output to docker terminal.
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]