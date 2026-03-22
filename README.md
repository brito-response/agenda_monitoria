## uv install dependences
```bash
    uv sync;
```

## activate env
```bash
    .\.venv\Scripts\activate
```

## run pylint
```bash
    uv run pylint --ignore=.venv,migrations,__pycache__,*.ini,*.toml ./ ;
    uv run black ./ --exclude ".venv|migrations|__pycache__|pyproject.toml|uv.lock|.pylintrc|.gitignore"
```

## init project django
```bash
    django-admin startproject agenda_monitoria ./
```

## init new app django
```bash
    python manage.py startapp nome_app
```

## create .env in root of project

```bash
SECRET_KEY=djangosecrets_of_project
DEBUG=True
NAME=novo_db
HOST=127.0.0.1
PORT=3306
USER=username
PASSWORD=password

```