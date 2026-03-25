## requirements
- python 3+
- dependency manager -> uv
- install
```bash
    irm https://astral.sh/uv/install.ps1 | iex
```
- Close and reopen the terminal and run:
```bash
    uv --version
```


## To run project:
- uv install dependences
```bash
    uv sync;
```

## activate env
```bash
    .\.venv\Scripts\activate
```

## create _.env_ in root of project
- gerator of secrets django [link](https://djecrety.ir/)

```bash
SECRET_KEY=djangosecrets_of_project
DEBUG=True
NAME=novo_db
HOST=127.0.0.1
PORT=3306
USER=username
PASSWORD=password

```

## Build the migrations and apply the migrations to the database.

```bash
    python manage.py makemigrations; python manage.py migrate; 

```

## create super user

```bash
    python manage.py createsuperuser; 

```

## run project

```bash
    python manage.py runserver # open another terminal and run
    python manage.py tailwindstart # to run tailwind in development

```

and good searching ...


# Utilities

## run pylint
```bash
    uv run pylint --ignore=.venv,migrations,__pycache__,*.ini,*.toml ./ ;
    uv run black ./ --exclude ".venv|migrations|__pycache__|pyproject.toml|uv.lock|.pylintrc|.gitignore"
```

