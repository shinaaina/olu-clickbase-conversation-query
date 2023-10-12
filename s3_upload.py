import csv
import clickhouse_connect
from io import StringIO
import boto3
from datetime import datetime
from clickhouse_driver import Client

def fetch_data_from_clickhouse():
    # Establish connection
    client = clickhouse_connect.get_client(host='yetbnhfay5.us-east-1.aws.clickhouse.cloud', port=8443, username='default', password='U_uI8vYuGK~PK')

    # Run your query
    result = client.query('SELECT * FROM conversations')
    print (result.result_rows)
    
    return result.result_rows
    
    
def write_to_s3(records, bucket_name, file_name):
    # Convert records to CSV string
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["customer_id", "conversation_id", "agent_id", "call_start", "call_end", "call_duration_sec", "call_status", "transcript", "sentiment_score", "keywords", "created_at", "updated_at"])  # header
    writer.writerows(records)
    
    # Get CSV data
    csv_data = output.getvalue()
    
    # Connect to S3 and upload
    s3_client = boto3.client('s3', aws_access_key_id='AKIA6KQYBA36QKVX7BUI',aws_secret_access_key='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')
    s3_client.put_object(Body=csv_data, Bucket=bucket_name, Key=file_name)

# Call the function to get the data
data = fetch_data_from_clickhouse()

# Generate filename based on today's date
current_date = datetime.now().strftime('%Y-%m-%d')
file_name = f"{current_date}.csv"

# Call the function to create CSV in s3
write_to_s3(data, "olu-cresta-bucket", file_name)
