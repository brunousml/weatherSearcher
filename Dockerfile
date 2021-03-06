FROM python:3.6.1-alpine

# We copy just the requirements.txt first to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ADD ./requirements.txt /app
ADD app/app.py /app
ADD ./entrypoint.sh /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create and set user
#RUN addgroup -g 1000 -S appuser && \
 #   adduser -u 1000 -S appuser -G appuser
#USER appuser

#RUN chown -R appuser:appuser /app
RUN chmod 777 /app

EXPOSE 5000

ENV FLASK_APP app.py
ENV FLASK_ENV development
CMD flask run
