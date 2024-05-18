#!/bin/bash
set -eux

ACC_NAME="cosmossqlacc"
RGROUP="cosmosdbrg"
DBNAME="firstdb"
CONTAINER="firstcontainer"

# create a sql api cosmos db account
# az cosmosdb create --name $ACC_NAME --resource-group $RGROUP

# create sql db
az cosmosdb sql database create \
  --resource-group $RGROUP \
  --account-name $ACC_NAME \
  --name $DBNAME

# create sql container
az cosmosdb sql container create \
  --resource-group $RGROUP \
  --account-name $ACC_NAME \
  --database-name $DBNAME \
  --name $CONTAINER \
  --partition-key-path "/employeeid"
