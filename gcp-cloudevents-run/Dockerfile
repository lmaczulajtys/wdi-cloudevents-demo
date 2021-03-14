FROM python:3.7-slim

ENV APP_HOME /app
ENV PYTHONUNBUFFERED TRUE

RUN pip install gunicorn cloudevents functions-framework

WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt

CMD ["functions-framework", "--target=handle_request"]
