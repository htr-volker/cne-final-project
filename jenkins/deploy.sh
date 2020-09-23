#!/bin/bash

error()
{
    echo "[ERROR]:" "$1" "EXITING"1>&2
    exit 1
}

warning()
{
    echo "[WARNING]:" "$1" 1>&2
}

output()
{
    echo "[OUTPUT]:" "$1" 1>&2
}


output "Deploying the database object"
kubectl apply -f ./pods/database.yaml

output "Delay NGINX start for 1 minute while waiting for frontend pods to start running"
sleep 1m

output "Deploying the backend object"
kubectl apply -f ./pods/backend.yaml

output "Deploying the gateway object"
kubectl apply -f ./pods/gateway.yaml

output "Deploying the frontend"
kubectl apply -f ./pods/frontend.yaml

output "Waiting 2 minute for health check of load balancer to compelete"
sleep 2m
