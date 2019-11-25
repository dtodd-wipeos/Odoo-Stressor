#!/bin/bash

build_name="alpine-python-app"

if [[ $EUID -ne 0 ]]; then
    echo "This script must be ran as root!"
    exit 1
fi

if [[ ! -f .env  ]]; then
    echo "Error, your environment is not correctly setup. Please create \`.env\` using \`sample.env\` for reference"
    exit 1
fi

echo "Removing previous container (if it exists, an error here is normal)"
docker ps -a | grep "${build_name}" | awk '{print $1}' | xargs docker rm

echo "Removing previous build (if it exists, an error here is normal)"
docker images | grep "${build_name}" | awk '{print $3}' | xargs docker rmi

echo "Building container with the files here"
docker build --tag ${build_name} .

echo "Running your app"
docker run --env-file .env ${build_name}
