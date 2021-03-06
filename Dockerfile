FROM python:3 as builder

COPY . /code
WORKDIR /code
RUN python -m unittest discover
RUN python setup.py sdist

FROM python:3 as tester

COPY features /features
RUN pip install -r /features/requirements.txt
COPY --from=builder /code/dist/ /tmp/artifacts
RUN pip install /tmp/artifacts/*
WORKDIR /features
RUN behave cli.feature

FROM python:3
COPY --from=builder /code/dist/ /tmp/artifacts
RUN pip install /tmp/artifacts/*

EXPOSE 5000
ENTRYPOINT record-manager-rest
CMD ["--port", "5000"]