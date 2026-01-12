docker exec namenode hdfs dfs -mkdir -p /datalake/bronze
docker exec namenode hdfs dfs -mkdir -p /datalake/silver
docker exec namenode hdfs dfs -mkdir -p /datalake/gold