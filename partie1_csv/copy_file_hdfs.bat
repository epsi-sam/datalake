REM Copier sur le namenode :
docker cp .\Datas\Heart_Attack\heart_attack_dataset.csv namenode:/tmp/

REM Dire au namenode d'enregistrer le fichier dans le HDFS :
docker exec namenode hdfs dfs -put /tmp/heart_attack_dataset.csv /data.csv

REM Ls 
docker exec namenode ls