#!/bin/bash
set -x
NODE_COUNT="1"
CLUSTER_NAME="aks-cluster-001"
CONTAINER_NAME="container-001"
RESOURCE_GROUP="Dev_School_Project"
VAULT_NAME="INGproject"
VAULT_USERNAME=$(az keyvault secret show --name User --vault-name "$VAULT_NAME" --query "value" -o tsv)
VAULT_PASSWORD=$(az keyvault secret show --name Password1 --vault-name "$VAULT_NAME" --query "value" -o tsv)
IMAGE_NAME="ing_project:latest"
ACR_NAME="astnp.azurecr.io"
PORT=5000

az aks create -g "$RESOURCE_GROUP" --name "$CLUSTER_NAME" --node-count "$NODE_COUNT" --generate-ssh-keys
az aks get-credentials -g "$RESOURCE_GROUP" --name "$CLUSTER_NAME"

kubectl get nodes

kubectl create secret docker-registry myregistrykey --docker-server="https://$ACR_NAME" --docker-username="$VAULT_USERNAME" --docker-password="$VAULT_PASSWORD"

cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
   name: "$CONTAINER_NAME"
spec:
   containers:
   - name: "$CONTAINER_NAME"
     image: "$ACR_NAME/$IMAGE_NAME"
   imagePullSecrets:
        - name: myregistrykey
EOF
sleep 30
kubectl exec "$CONTAINER_NAME" -- sh health_check.sh