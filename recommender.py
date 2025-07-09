import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import boto3
import os

# Load the dataset
df = pd.read_csv("dataset/spotify_audio_features.csv", encoding='latin1')

# Features to use
features = [
    'danceability', 'energy', 'valence', 'tempo',
    'liveness', 'speechiness', 'acousticness', 'instrumentalness'
]

# Ensure required columns are present
df = df.dropna(subset=features + ['track_name', 'artist_name'])

# Prepare feature matrix
scaler = StandardScaler()
X = scaler.fit_transform(df[features])


def detect_mood_with_comprehend(text):
    comprehend = boto3.client(
        'comprehend',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name="us-east-1"
    )
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment'].lower()
    confidence = response['SentimentScore'][sentiment.title()]
    return sentiment, round(confidence * 100, 2)


def recommend_song(song_title=None, include_input=True, mood=None, return_meta=False):
    filtered_df = df.copy()

    detected_mood = ""
    confidence = None

    # Detect mood from text if mood not explicitly passed
    if not mood and song_title:
        detected_mood, confidence = detect_mood_with_comprehend(song_title)
        mood = detected_mood
    elif mood:
        detected_mood = mood
        confidence = None

    # Mood filters (can be expanded)
    if mood:
        mood = mood.lower()
        if mood == 'happy':
            filtered_df = filtered_df[filtered_df['valence'] > 0.6]
        elif mood == 'sad':
            filtered_df = filtered_df[filtered_df['valence'] < 0.4]
        elif mood == 'energetic':
            filtered_df = filtered_df[filtered_df['energy'] > 0.6]
        elif mood == 'calm':
            filtered_df = filtered_df[filtered_df['energy'] < 0.4]

    filtered_df = filtered_df.reset_index(drop=True)

    # If no song provided, return top 10
    if not song_title or song_title not in filtered_df['track_name'].values:
        recommendations = [
            {
                "track_name": row['track_name'],
                "artist": row['artist_name'],
                "spotify_link": row.get("spotify_link", "#")
            }
            for _, row in filtered_df.head(10).iterrows()
        ]
        if return_meta:
            return recommendations, detected_mood, confidence
        else:
            return recommendations

    # Find index of input song
    idx = filtered_df[filtered_df['track_name'] == song_title].index[0]
    X_filtered = scaler.fit_transform(filtered_df[features])
    similarities = cosine_similarity([X_filtered[idx]], X_filtered)[0]

    # Top similar songs
    top_indices = similarities.argsort()[::-1][1:11]  # skip original
    recommendations = []
    for i in top_indices:
        row = filtered_df.iloc[i]
        recommendations.append({
            "track_name": row['track_name'],
            "artist": row['artist_name'],
            "spotify_link": row.get("spotify_link", "#")
        })

    if return_meta:
        return recommendations, detected_mood, confidence
    else:
        return recommendations
