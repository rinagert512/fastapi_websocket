FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add python3-dev gcc g++ libc-dev

WORKDIR /usr/src/app
ADD requirements.txt .
RUN mkdir data

RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]