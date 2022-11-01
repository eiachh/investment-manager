FROM python:latest

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
ADD . /app
WORKDIR /app

EXPOSE 5004

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]