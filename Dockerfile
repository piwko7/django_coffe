# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y  gettext
WORKDIR /code
RUN pip install pipenv
COPY Pipfile* /code/
RUN pipenv sync --system
COPY . /code/


#CMD ["uvicorn", "--factory", "--host", "0.0.0.0", "--port", "8000", "ipos.main:create_app"]