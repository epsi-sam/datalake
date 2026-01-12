# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import time

# Initialisation
spark = SparkSession.builder.appName("ConversionToParquet").getOrCreate()

# Réduire le logging Spark
spark.sparkContext.setLogLevel("ERROR")

# Lecture HDFS
df = spark.read.csv("hdfs://namenode:9000/data.csv", header=True, inferSchema=True)

# Convserion au format Parquet
df.write.mode("overwrite").parquet("hdfs://namenode:9000/heart_data.parquet")


spark.stop()