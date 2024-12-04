import boto3
import json

# Initialize Personalize client
personalize = boto3.client('personalize')

def create_dataset_import_job(dataset_arn, data_location, role_arn, job_name):
    """
    Creates a dataset import job in Amazon Personalize.
    """
    response = personalize.create_dataset_import_job(
        jobName=job_name,
        datasetArn=dataset_arn,
        dataSource={'dataLocation': data_location},
        roleArn=role_arn
    )
    return response

if __name__ == "__main__":
    # Replace with your dataset ARN, S3 data location, and IAM role ARN
    DATASET_ARN = "arn:aws:personalize:region:account-id:dataset/interactions"
    DATA_LOCATION = "s3://your-bucket/interactions.csv"
    ROLE_ARN = "arn:aws:iam::account-id:role/PersonalizeRole"
    JOB_NAME = "InteractionsImportJob"

    response = create_dataset_import_job(DATASET_ARN, DATA_LOCATION, ROLE_ARN, JOB_NAME)
    print("Dataset Import Job Created:", json.dumps(response, indent=2))