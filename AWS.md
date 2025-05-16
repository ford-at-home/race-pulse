# AWS Architecture for Race Pulse

## 🧩 Recommended Services

| Purpose                  | Service          |
|-------------------------|------------------|
| Code hosting            | CodeCommit / GitHub
| API endpoint            | API Gateway      |
| Inference logic         | Lambda           |
| Static site/dashboard   | S3 + CloudFront  |
| Metrics/alerts          | CloudWatch       |
| Secret storage          | Secrets Manager  |
| Model training (future) | SageMaker        |
| CI/CD                   | CodePipeline / GitHub Actions |

## 🛠️ Architecture Summary
1. Upload time-series data to S3.
2. Trigger Lambda via API Gateway or S3 event.
3. Lambda uses the model to return predictions.
4. Results shown via S3-hosted dashboard or returned by API.

## ☁️ Additional Enhancements
- Use EventBridge for scheduling batch jobs
- Add DynamoDB if storing user sessions or race logs
- Use Step Functions for chaining ETL + prediction logic
