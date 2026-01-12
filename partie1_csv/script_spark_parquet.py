# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import time

# Initialisation
spark = SparkSession.builder.appName("AnalysePARQUET").getOrCreate()

# Réduire le logging Spark
spark.sparkContext.setLogLevel("ERROR")

# Import du fichier en format parquet
df_parquet = spark.read.parquet("hdfs://namenode:9000/heart_data.parquet")

debut = time.time()
# Calculs de quelques données
df_parquet.select("Age", "Cholesterol", "BloodPressure", "BMI").describe().show()

# Calcul : Moyenne cholestérol par genre
df_parquet.groupBy("Gender").avg("Cholesterol").show()
print("Temps ecoule : ")
print(time.time() - debut)
