output "s3_bucket_name" {
  value       = aws_s3_bucket.email_bucket.bucket
  description = "The name of the S3 bucket used for storing email lists."
}

output "lambda_function_name" {
  value       = aws_lambda_function.send_email_lambda.function_name
  description = "The name of the Lambda function used for sending emails."
}

output "lambda_function_arn" {
  value       = aws_lambda_function.send_email_lambda.arn
  description = "The ARN of the Lambda function used for sending emails."
}

output "iam_role_arn" {
  value       = aws_iam_role.lambda_iam_role.arn
  description = "The ARN of the IAM role assigned to the Lambda function."
}
