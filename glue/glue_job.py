from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("RideETL").getOrCreate()

# Read raw data from S3
df = spark.read.csv(
    "s3://your-bucket-name/raw/ride_data.csv",
    header=True,
    inferSchema=True
)

# Data Quality Checks
df = df.dropna()

# Transformations
df = df.withColumn("timestamp", to_timestamp("timestamp"))
df = df.withColumn("year", year("timestamp"))
df = df.withColumn("month", month("timestamp"))

# Aggregation (Business logic)
df_agg = df.groupBy("city", "year", "month").agg(
    sum("fare").alias("total_revenue"),
    count("ride_id").alias("total_rides"),
    avg("fare").alias("avg_fare")
)

# Write to S3 (Processed Layer)
df_agg.write.mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("s3://your-bucket-name/processed/ride_data/")

print("🚀 Glue Job Completed")
