FROM python:3.7-alpine
WORKDIR /app
COPY ../requirements.txt /app
RUN pip3 install -r requirements.txt
COPY .. /app
ENV FLASK_APP=api
ENV FLASK_ENV=production
ENTRYPOINT ["flask"]
CMD ["run", "-h", "0.0.0.0"]