#!/bin/bash
set -x
CONTAINER_NAME="container-001"
CONTAINER_DNS_NAME=$(echo "$CONTAINER_NAME"-dns)
RESOURCE_GROUP="Dev_School_Project"
VAULT_NAME="INGproject"
VAULT_USERNAME=$(az keyvault secret show --name User --vault-name "$VAULT_NAME" --query "value" -o tsv)
VAULT_PASSWORD=$(az keyvault secret show --name Password1 --vault-name "$VAULT_NAME" --query "value" -o tsv)
IMAGE_NAME="astnp.azurecr.io/ing_project:latest"
PORT=5000

az container create -g "$RESOURCE_GROUP" --name "$CONTAINER_NAME" --image "$IMAGE_NAME" --cpu 1 --memory 1 --registry-login-server astnp.azurecr.io --registry-username "$VAULT_USERNAME" --registry-password "$VAULT_PASSWORD" --ip-address Public --dns-name-label "$CONTAINER_DNS_NAME" --ports "$PORT"

script --return --quiet -c "az container exec -g $RESOURCE_GROUP --name $CONTAINER_NAME --exec-command 'sh health_check.sh'" /dev/null