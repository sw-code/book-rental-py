@echo off
echo Zum Stoppen
pause
kubectl delete -f .\02_Postgres.yaml -n ingress-nginx
kubectl delete -f .\03_Django.yaml -n ingress-nginx
kubectl delete -f .\04_Ingress.yaml -n ingress-nginx
