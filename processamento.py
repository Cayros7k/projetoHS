from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Lendo arquivo CSV do Hadoop") \
    .master("local") \
    .getOrCreate()

file_path = "hdfs://localhost:9000/cay/client_data.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

df.show(5)