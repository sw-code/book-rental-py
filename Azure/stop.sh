#!/bin/sh
kubectl delete -f .\02_Postgress.yaml
kubectl delete -f .\03_Django.yaml
