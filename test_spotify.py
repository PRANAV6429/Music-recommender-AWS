import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

query = "Shape of You Ed Sheeran"
result = sp.search(q=query, type='track', limit=1)

if result['tracks']['items']:
    print("✅ API working!")
    print("Preview URL:", result['tracks']['items'][0]['preview_url'])
else:
    print("❌ No results from Spotify")
