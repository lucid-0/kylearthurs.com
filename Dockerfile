FROM python:3.8

RUN apt-get update -y && apt-get upgrade -y && pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# RUN ln $HOME/.poetry/bin/poetry /bin/poetry
# RUN poetry config virtualenvs.create false --local
# RUN poetry self update
# RUN poetry install
