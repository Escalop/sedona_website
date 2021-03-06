# Intership 13/12/2021

Cookiecutter template for GarpixCMS == 1.0.0.

## Install

1. Install Docker, docker-compose. 
For Debian, Ubuntu:
```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
```
Install pipenv as well
Don't forget press CTRL+D to exit from super user account.

2. Apply environment variables:

```
cp example.env .env
```

3. Change a random string for `SECRET_KEY` and `POSTGRES_PASSWORD` in `.env`.

4. Install dependencies:

```
pipenv install
pipenv shell
```

5. Up docker-compose, migrate database and create super user:

```
docker-compose up -d
python3 backend/manage.py makemigrations
python3 backend/manage.py migrate
python3 backend/manage.py createsuperuser
```
6. Run the server:
```
python3 backend/manage.py runserver
```