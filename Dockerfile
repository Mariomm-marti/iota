FROM alpine:3.20.3 AS base

WORKDIR /opt/iota
RUN apk add python3=~3.12 py3-pip
RUN pip install pipenv --break-system-packages
COPY Pipfile Pipfile.lock /opt/iota/
RUN pipenv install

FROM base AS test

COPY --from=base /opt/iota/Pipfile /opt/iota/Pipfile.lock /opt/iota/
RUN pipenv install --dev
COPY . /opt/iota
ENTRYPOINT [ "/usr/bin/pipenv", "run", "pytest" ]
CMD [ "." ]

FROM base AS prod

COPY iota/ /opt/iota
ENTRYPOINT [ "/usr/bin/pipenv", "run", "uvicorn", "main:app" ]
CMD [ "--host", "0.0.0.0", "--port", "4242", "--workers", "4" ]
