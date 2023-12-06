import boto3
import csv
import io
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    ses_client = boto3.client('ses')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        file_content = s3_client.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')
    except ClientError as e:
        print(e)
        return {"statusCode": 500, "body": json.dumps("Error in getting object from S3")}

    reader = csv.reader(io.StringIO(file_content))
    next(reader)  
    for row in reader:
        if len(row) > 2:
            try:
                response = ses_client.send_email(
                    Source='whatever@example.com', # Change your sender email here (it has to be verified). #
                    Destination={'ToAddresses': [row[2].strip()]},
                    Message={
                        'Subject': {'Data': 'Hello', 'Charset': 'UTF-8'},
                        'Body': {'Text': {'Data': 'How are you?', 'Charset': 'UTF-8'}}
                    }
                )
                print(f"Email sent to {row[2].strip()}: {response}")
            except ClientError as e:
                print(f"Failed to send email to {row[2].strip()}: {e}")

    return {"statusCode": 200, "body": json.dumps("Emails sent successfully.")}
