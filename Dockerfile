FROM python:3.8-alpine
ARG API_KEY_ARG
ENV API_KEY = $API_KEY_ARG
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]