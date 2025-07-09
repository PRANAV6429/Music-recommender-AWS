import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Load AWS credentials
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Create AWS Comprehend client
comprehend = boto3.client(
    'comprehend',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def detect_mood(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment'].lower()

    # Map AWS sentiment to app mood
    mood_map = {
        'positive': 'happy',
        'negative': 'sad',
        'neutral': 'calm',
        'mixed': 'energetic'
    }

    mood = mood_map.get(sentiment, 'calm')
    return mood, response['SentimentScore']

# Test it
if __name__ == "__main__":
    user_input = input("How are you feeling today? → ")
    mood, scores = detect_mood(user_input)
    print(f"Detected Mood: {mood}")
    print("Confidence Scores:", scores)
