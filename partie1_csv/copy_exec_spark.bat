REM copy spark script on docker
docker cp partie1_csv/script_spark_csv.py spark-master:/tmp/script_spark_csv.py
docker cp partie1_csv/script_spark_conversion.py spark-master:/tmp/script_spark_conversion.py
docker cp partie1_csv/script_spark_parquet.py spark-master:/tmp/script_spark_parquet.py

REM run CSV using spark-submit (not on PATH)
docker exec spark-master /spark/bin/spark-submit ^
  --master spark://spark-master:7077 ^
  /tmp/script_spark_csv.py

REM run CONVERSION using spark-submit (not on PATH)
docker exec spark-master /spark/bin/spark-submit ^
  --master spark://spark-master:7077 ^
  /tmp/script_spark_conversion.py

REM run PARQUET using spark-submit (not on PATH)
docker exec spark-master /spark/bin/spark-submit ^
  --master spark://spark-master:7077 ^
  /tmp/script_spark_parquet.py
