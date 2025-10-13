@echo off
kubectl apply -f .\01_PV-PVC.yaml -n ingress-nginx
kubectl apply -f .\02_Postgres.yaml -n ingress-nginx
timeout 10
kubectl apply -f .\03_Django.yaml -n ingress-nginx
kubectl apply -f .\04_Ingress.yaml -n ingress-nginx
