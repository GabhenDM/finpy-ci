FROM python:3.8-alpine
WORKDIR /project
ENV PYTHONUNBUFFERED=0
ENV API_KEY=
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV API_URL=https://finnhub.io/api/v1/
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run","--host=0.0.0.0"]