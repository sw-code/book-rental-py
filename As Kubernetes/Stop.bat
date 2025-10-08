@echo off
echo Zum Stoppen
pause

kubectl delete -f .\05_Deploy_Django.yaml
::kubectl delete -f .\04_1_MakeMigrations.yaml
kubectl delete -f .\04_0_Start_Postgres.yaml
kubectl delete -f .\03_Create_Start_Services.yaml
kubectl delete -f .\02_Create_PVC.yaml
kubectl delete -f .\01_Create_PV.yaml