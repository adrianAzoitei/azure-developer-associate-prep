#!/bin/bash

az group create -n cert-prep-webapps-rg -l westeurope

az appservice plan create --name cert-prep-webapps-dev-plan \
  --resource-group cert-prep-webapps-rg \
  --sku s1 \
  --is-linux

az webapp create -g cert-prep-webapps-rg \
  -p cert-prep-webapps-dev-plan \
  -n prep123webapp \
  --runtime "node|20.10"

