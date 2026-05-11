🚀 Spark on AWS EMR – Orders ETL Pipeline
📌 Overview

This project demonstrates a simple Data Engineering pipeline using PySpark on Amazon EMR.

The pipeline:

Reads raw order data from S3
Performs transformations using PySpark
Writes optimized output back to S3 in Parquet format with Snappy compression

🏗️ Architecture
S3 (Input CSV) → EMR (PySpark Job) → S3 (Parquet Output)

⚙️ Tech Stack
AWS EMR (Spark)
PySpark
Amazon S3
Parquet (Snappy Compression)

📂 Project Structure
.
├── data/
│   └── orders.csv
├── scripts/
│   └── orders_pyspark_job.py
├── architecture.png
└── README.md

📥 Input Data
Sample dataset:

order_id
customer_id
amount
category
order_date

Stored in:
s3://<your-bucket>/input/orders.csv

🔄 ETL Process
1. Extract
Read CSV data from S3
2. Transform
Select relevant columns
Aggregate total spend per customer
3. Load
Write output to S3 in Parquet format
Apply Snappy compression

🧠 Key Features
Distributed processing using Spark
Cost-efficient storage with Parquet + Snappy
Scalable architecture using EMR
Clean separation of input, scripts, and output

▶️ How to Run
1. Upload files to S3
s3://<your-bucket>/input/orders.csv
s3://<your-bucket>/scripts/orders_pyspark_job.py
2. Create EMR Cluster
Application: Spark
Instance type: m5.large or m5.xlarge
3. Add Step
Step type: Spark application
Script location:
s3://<your-bucket>/scripts/orders_pyspark_job.py

📤 Output
Stored in:
s3://<your-bucket>/output/customer_spend/

Contains:
Parquet files (Snappy compressed)
_SUCCESS flag