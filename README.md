# Aws-uber-ridedata-pipeline

 AWS uber Ride Data Pipeline 🚕

 Overview
End-to-end AWS data engineering pipeline using S3, Glue (PySpark), and Athena.

---

 Architecture
CSV → S3 (Raw) → Glue ETL → S3 (Processed - Parquet) → Athena

---

 Tech Stack
- AWS S3
- AWS Glue (PySpark)
- AWS Athena
- Python (Boto3)

---

 Features
- ETL pipeline using PySpark
- Partitioned data (year/month)
- Serverless analytics with Athena
- Data quality handling

---

 How to Run

1. Upload data:
```
python scripts/upload_to_s3.py
```

2. Run Glue Job (AWS Console)

3. Query using Athena

---

 Insights
- Revenue by city
- Monthly ride trends
- Average fare analysis

---
