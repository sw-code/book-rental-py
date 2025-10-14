@echo off
kubectl apply -f .\01_Create_PV.yaml
kubectl apply -f .\02_Create_PVC.yaml
kubectl apply -f .\03_Create_Start_Services.yaml
kubectl apply -f .\04_0_Start_Postgres.yaml
timeout 10
::kubectl apply -f .\04_1_MakeMigrations.yaml
kubectl apply -f .\05_Deploy_Django.yaml

::echo Zum Beenden des Migration Continers
::pause
::kubectl delete -f .\04_1_MakeMigrations.yaml