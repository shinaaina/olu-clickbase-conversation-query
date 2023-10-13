# olu-conversation-query
olu-conversation-query
This repo contains these 3 files to meet the requirements of the customer:

- SQL Query to fetch data from Clickhouse. "data_query.sql"
- Python code that runs the SQL query, stores the data into a CSV file, and uploads to an AWS S3 Bucket. "s3_upload.py"
- A GitHub Action to schedule the execution of the Python code daily.

**Other Points to note:**
1. The Python code has the following parameters that should be changed to values for the respoective environments:
- Click House Connection details:
  - hostname
  - port
  - username
  - password

- AWS Credentials:
  - S3 Bucket name
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY

- CSV File Name dynamic set to "Daily Agent Report {Today's date}.csv

2. The GitHub Action has been set to run at 23:00 GMT everyday, and can be changed based on preference
3. The GitHub Action can also be run manually for testing or adhoc requests.
