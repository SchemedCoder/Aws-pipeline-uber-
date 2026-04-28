import boto3

# Replace with your bucket name
BUCKET_NAME = "your-bucket-name"
FILE_PATH = "../data/ride_data.csv"
S3_KEY = "raw/ride_data.csv"

def upload():
    s3 = boto3.client("s3")

    try:
        s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
        print("✅ File uploaded to S3")
    except Exception as e:
        print("❌ Upload failed:", e)

if __name__ == "__main__":
    upload()
