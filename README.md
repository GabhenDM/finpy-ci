# Finpy - Continuous Integration with Github Actions project

[![Finpy-CI Actions Status](https://github.com/GabhenDM/finpy-ci/workflows/Finpy-CI/badge.svg)](https://github.com/GabhenDM/finpy-ci/actions)

This is a training project utilizing Flask and the [finnhub](finnhub.io) API for a full CI/CD cycle with Github actions, including unit testing, Code quality scanning (Sonarqube) and Slack notifications for building of Docker images.

** Libraries and Packages utilized **

- Flask
- Pytest
- Requests
- python-dotenv

<br>

## Usage

``` shell
docker run -d -p 80:5000 -e API_KEY='<INSERT finnhub.io API KEY here>' robijndm/finpy-ci
```