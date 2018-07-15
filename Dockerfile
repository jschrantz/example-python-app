FROM python:3 as builder

COPY . /code
WORKDIR /code
RUN python -m unittest discover
RUN python setup.py sdist

FROM python:3
COPY --from=builder /code/dist/ /tmp/artifacts
RUN pip install /tmp/artifacts/*

ENTRYPOINT record-manager
CMD ["--help"]