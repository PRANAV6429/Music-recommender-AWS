import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("dataset/spotify_audio_features.csv", encoding='latin1')

# Features to use
features = [
    'danceability',
    'energy',
    'valence',
    'tempo',
    'liveness',
    'speechiness',
    'acousticness',
    'instrumentalness'
]

# Clean rows
df_clean = df.dropna(subset=features)
df_clean = df_clean.reset_index(drop=True)

# Normalize
scaler = StandardScaler()
X = scaler.fit_transform(df_clean[features])

# 💡 Function to recommend songs based on one input
def recommend_song(input_title, top_n=5):
    if input_title not in df_clean['track_name'].values:
        print(f"❌ Song '{input_title}' not found in dataset.")
        return

    idx = df_clean[df_clean['track_name'] == input_title].index[0]
    input_vector = X[idx].reshape(1, -1)
    
    # Compute similarity only with one row
    similarities = cosine_similarity(input_vector, X).flatten()
    
    # Get top N similar (excluding self)
    similar_indices = similarities.argsort()[::-1][1:top_n+1]

    print(f"\n🎧 Recommendations for: {input_title}")
    for i in similar_indices:
        title = df_clean.iloc[i]['track_name']
        artist = df_clean.iloc[i]['artist_name']
        print(f" - {title} by {artist}")

# ✅ TEST IT
recommend_song("Shape of You")
