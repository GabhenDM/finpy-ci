FROM python:3.6-alpine3.7
ARG API_KEY_ARG
ENV API_KEY = $API_KEY_ARG
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["flask", "run"]