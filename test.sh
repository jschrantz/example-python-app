#!/bin/bash -e

# This is a simple helper script to allow running the component tests for the
# REST server for example purposes. I'd typically split the build and testing
# pieces in an automated pipeline, but this should be an easier entrypoint


function cleanup {
    set +e
    docker rm -f record_manager
    docker rmi record_manager record_manager_tester
}

trap cleanup EXIT

# Runs the unit tests, python package, cli behave component tests, and produces
# a deployable docker image

docker build -t record_manager .

# Removes any previously running container named record_manager
set +e
docker rm -f record_manager
set -e

# Starts a record_manager container
docker run -d --name record_manager record_manager

# Build a tester image for the component tests of the rest service
docker build -t record_manager_tester features/

docker run -it --rm -v $(pwd)/features:/features \
           --link record_manager:app \
           --workdir /features \
           record_manager_tester behave rest.feature
