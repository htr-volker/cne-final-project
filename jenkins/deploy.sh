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
kubectl apply -f ./k8s/database.yaml

output "Wait for database to finish initialising"
sleep 1m

output "Deploying the backend object"
kubectl apply -f ./k8s/backend.yaml

output "Deploying the gateway object"
kubectl apply -f ./k8s/gateway.yaml

output "Deploying the frontend"
kubectl apply -f ./k8s/frontend.yaml

output "Waiting 2 minute for health check of load balancer to compelete"
sleep 2m
