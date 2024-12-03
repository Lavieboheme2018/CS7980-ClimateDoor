
import base64
import json
import boto3
import logging
from botocore.exceptions import ClientError
from datetime import datetime

# Initialize the Personalize Events client
personalize_events_client = boto3.client('personalize-events', region_name='us-west-2')
TRACKING_ID = ""  # Add the tracking ID for Tool

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function to process DynamoDB stream records and send interactions to Amazon Personalize.
    """
    for record in event['Records']:
        try:
            # Ensure the event is an "INSERT" event from DynamoDB
            if record['eventName'] != 'INSERT' or record['eventSource'] != 'aws:dynamodb':
                logger.info("Skipping non-INSERT or non-DynamoDB event.")
                continue

            # Extract data from DynamoDB stream event
            new_image = record['dynamodb'].get('NewImage', {})
            user_id = new_image.get('user_id', {}).get('S')
            event_type = new_image.get('event_type', {}).get('S')
            item_id = new_image.get('item_id', {}).get('S')
            timestamp = new_image.get('timestamp', {}).get('S')

            # Check for required fields
            if not user_id or not event_type or not item_id or not timestamp:
                logger.warning(f"Skipping record due to missing required fields: {new_image}")
                continue

            # Convert timestamp to milliseconds
            sent_at = int(timestamp) * 1000

            # Construct the event list for Personalize based on the schema
            event_list = [{
                'sentAt': sent_at,
                'eventType': event_type,
                'properties': json.dumps({"ITEM_ID": item_id})  # Align with the schema ITEM_ID field
            }]

            # Send the event to Amazon Personalize
            response_code = put_tool_events(TRACKING_ID, user_id, "default-session", event_list)
            logger.info(f"Response code: {response_code}")

        except ClientError as e:
            logger.error(f"Client error: {e.response['Error']['Message']}")
        except Exception as e:
            logger.error(f"Error processing record: {str(e)}")

    return {'statusCode': 200, 'body': json.dumps('Lambda processed successfully')}

def put_tool_events(tracking_id, user_id, session_id, event_list):
    """
    Helper function to send events to Amazon Personalize.
    """
    try:
        response = personalize_events_client.put_events(
            trackingId=tracking_id,
            userId=user_id,
            sessionId=session_id,
            eventList=event_list
        )
        return response['ResponseMetadata']['HTTPStatusCode']
    except ClientError as e:
        logger.error(f"Error sending events to Personalize: {e}")
        raise
