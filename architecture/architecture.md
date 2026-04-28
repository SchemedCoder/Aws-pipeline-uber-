 AWS Ride Data Pipeline Architecture 

 Flow

1. Raw Layer (Amazon S3)
- Store raw CSV files

2. Processing Layer (AWS Glue)
- PySpark ETL job
- Data cleaning + transformations
- Partitioning (year/month)

3. Processed Layer (S3 - Parquet)
- Optimized storage
- Partitioned for fast queries

4. Analytics Layer (Athena)
- SQL queries on S3 data

---

 Why This Design?

- Scalable (handles large data)
- Serverless (low cost)
- Fast querying (Parquet + partitions)

---

 Key Concepts

- Data Lake (S3)
- ETL (Glue)
- Partitioning
- Serverless Analytics (Athena)
