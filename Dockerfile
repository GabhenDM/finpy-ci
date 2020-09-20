FROM python:3.6-alpine3.7
WORKDIR /project
ENV FLASK_ENV=production
ADD . /project
RUN pip install -r requirements.txt
CMD ["flask", "run"]