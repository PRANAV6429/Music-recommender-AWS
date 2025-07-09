import boto3
import os
import uuid
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Load credentials
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Create DynamoDB client
dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Reference your table
table = dynamodb.Table('MoodLogs')

def log_mood_to_dynamodb(user_message, detected_mood):
    try:
        response = table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'user_message': user_message,
                'detected_mood': detected_mood,
                'timestamp': datetime.utcnow().isoformat()
            }
        )
        print("[OK] Mood log saved to DynamoDB.")
    except Exception as e:
        print("[NO] Failed to save to DynamoDB:", e)
