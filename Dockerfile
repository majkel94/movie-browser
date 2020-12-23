FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/dev/.local/bin/:${PATH}"

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app/
RUN chmod +x /app/scripts

RUN useradd -ms /bin/bash dev
USER dev


