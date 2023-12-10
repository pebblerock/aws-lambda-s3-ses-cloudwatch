# Event-Driven AWS Lambda & S3 Email Service

This repository hosts a Terraform-managed, event-driven infrastructure on AWS, designed to trigger a Lambda function that upon .csv file uploads to an S3 bucket, sends bulk emails using AWS Simple Email Service. The project  integrates AWS S3, Lambda, and SES, showcasing an efficient, serverless architecture responsive to real-time events. It can be used for automated email marketing campaigns.

# AWS Infrastructure Diagram

![AWS Diagram](/aws-diagram.png) 

# How it works

1. **Creating an S3 Bucket**: First the script creates a bucket in AWS S3. The bucket is named "csvs3lambdaemailbucket". This is where the .csv file containing the emails will be uploaded to trigger the email sending process.

2. **Setting Up a Lambda Function**: The Lambda function is called "S3LambdaSES" and it's written in Python. The function's job is to send out emails. Its code is packaged in a file named "lambda_function.zip". This is known as a deployment package.

3. **Creating an IAM Role for Lambda**: For the Lambda function to work it needs the right permissions. This script sets up an IAM (Identity and Access Management) role called "lambda_execution_role". This role gives the Lambda function the necessary permissions to run and access other AWS resources such as CloudWatch, S3 and SES.

4. **IAM Role Policies**: This step is about defining what the Lambda function can do. The policies allow it to write logs, send emails using AWS SES (Simple Email Service) and read/write from the S3 bucket.

5. **Lambda Permissions for S3 Bucket**: The script gives permission for the S3 bucket to trigger the Lambda function. This means whenever a new file is uploaded to the bucket the Lambda function will run.

6. **Setting Up S3 Bucket Notifications**: Finally, this part sets up the bucket so that it sends a notification to the Lambda function every time a new object is created in it. This is what starts the process of sending an email.

# How to use the Terraform IaC.

## Prerequisites.

Disclaimer: By default, AWS SES is in a sandbox environment and you will be limited to sending 200 emails per day and all recipients must be verified when you are using the script. You can request a removal in which case you do not need to verify receiver emails and increase your email limit.

This script does not send emails from a domain but an ordinary email. To use this script you have to:

1. Verify the email you are sending from in the AWS Console. SES > Verified identities.
2. Go to lambda/lambda_function.py file and change the example email (whatever@example.com) to the verified email you are sending from.
3. Zip the lambda folder containing the lambda_function.py and place the zip in the same folder. The .zip file is the deployment package.
4. Navigate to the terraform folder and launch the IaC.
3. Upload the email.csv to the S3 bucket. If you are still in the sandbox environment, make sure the receiver emails are verified.