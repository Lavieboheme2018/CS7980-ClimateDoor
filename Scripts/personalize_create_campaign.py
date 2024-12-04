import boto3
import json

# Initialize Personalize client
personalize = boto3.client('personalize')

def create_campaign(solution_version_arn, campaign_name, min_tps=1):
    """
    Creates a campaign in Amazon Personalize.
    """
    response = personalize.create_campaign(
        name=campaign_name,
        solutionVersionArn=solution_version_arn,
        minProvisionedTPS=min_tps
    )
    return response

if __name__ == "__main__":
    # Replace with your solution version ARN and campaign name
    SOLUTION_VERSION_ARN = "arn:aws:personalize:region:account-id:solution-version/user-personalization-solution-version"
    CAMPAIGN_NAME = "UserPersonalizationCampaign"

    response = create_campaign(SOLUTION_VERSION_ARN, CAMPAIGN_NAME)
    print("Campaign Created:", json.dumps(response, indent=2))