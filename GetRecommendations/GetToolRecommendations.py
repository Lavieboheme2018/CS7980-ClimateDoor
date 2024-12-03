
import boto3
import json

# Initialize the Personalize runtime client
personalizeRt = boto3.client('personalize-runtime')

def get_tool_recommendations_for_user(campaign_arn, user_id, num_results):
    """
    Helper function to get recommendations for a user.
    """
    response = personalizeRt.get_recommendations(
        campaignArn=campaign_arn,
        userId=user_id,
        numResults=num_results
    )

    # Extract the recommended items from the response
    recommended_items = [{{'ItemId': item['itemId']}} for item in response['itemList']]

    return recommended_items

def lambda_handler(event, context):
    try:
        # Extract parameters from the mapped payload
        user_id = event.get('userId')
        if not user_id:
            raise KeyError("userId")

        # Replace with the specific campaign ARN for Tools
        campaign_arn = event.get('campaignArn')  # No default value set; must be provided

        num_results = int(event.get('numResults', 10))

        # Call Personalize to get recommendations
        recommended_items = get_tool_recommendations_for_user(campaign_arn, user_id, num_results)

        # Return the recommended items in the response
        return {{
            'statusCode': 200,
            'body': json.dumps({{
                'recommendedItems': recommended_items
            }})
        }}

    except KeyError as e:
        return {{
            'statusCode': 400,
            'body': json.dumps(f"Missing required parameter: {{e}}")
        }}
    except Exception as e:
        print(f"Error getting recommendations: {{e}}")
        return {{
            'statusCode': 500,
            'body': json.dumps(f"Error getting recommendations: {{e}}")
        }}
