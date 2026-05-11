from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Initialize Spark session
spark = SparkSession.builder.appName("OrdersETLJob").getOrCreate()

# Input and Output paths (update bucket name before running)
input_path = "s3://emr-demo-pyspark/input/orders.csv"
output_path = "s3://emr-demo-pyspark/output/customer_spend/"

# Load data
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Basic transformation: select required columns
df = df.select("customer_id", "amount")

# Aggregate: total spend per customer
result = df.groupBy("customer_id").agg(sum("amount").alias("total_spent"))

# Optimization: reduce number of output files
result = result.repartition(1)

# Write output in Parquet format
result.write.mode("overwrite").option("compression", "snappy").parquet(output_path)

print("Job completed successfully!")

spark.stop()
