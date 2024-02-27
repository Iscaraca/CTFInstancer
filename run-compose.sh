#!/bin/sh

dockerd &
sleep 5

export PORT=$2

docker compose -p $1 up -d --build

sleep 600

docker compose -p $1 down --volumes