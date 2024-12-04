import boto3
import json

# Initialize Personalize client
personalize = boto3.client('personalize')

def create_solution_version(solution_arn):
    """
    Triggers the training of a solution in Amazon Personalize.
    """
    response = personalize.create_solution_version(solutionArn=solution_arn)
    return response

if __name__ == "__main__":
    # Replace with your solution ARN
    SOLUTION_ARN = "arn:aws:personalize:region:account-id:solution/user-personalization-solution"

    response = create_solution_version(SOLUTION_ARN)
    print("Solution Training Triggered:", json.dumps(response, indent=2))