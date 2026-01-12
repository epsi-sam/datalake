# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import time

# Initialisation
spark = SparkSession.builder.appName("AnalyseCSV").getOrCreate()

# Réduire le logging Spark
spark.sparkContext.setLogLevel("ERROR")

# Lecture HDFS
df = spark.read.csv("hdfs://namenode:9000/data.csv", header=True, inferSchema=True)

# Calculs de quelques données
df.select("Age", "Cholesterol", "BloodPressure", "BMI").describe().show()

# Calcul : Moyenne cholestérol par genre
df.groupBy("Gender").avg("Cholesterol").show()


spark.stop()