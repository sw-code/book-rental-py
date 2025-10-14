@echo off
kubectl apply -f .\00_NameSpace.yaml
kubectl apply -f .\01_PV-PVC.yaml
kubectl apply -f .\02_Postgress.yaml
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.19.0/cert-manager.yaml
timeout 10
kubectl apply -f .\03_Django.yaml
kubectl apply -f .\04_Ingress.yaml