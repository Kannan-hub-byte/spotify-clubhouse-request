import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

# Read tokens from file
def read_tokens(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Path to the tokens file
tokens_file = "tokens.txt"
tokens = read_tokens(tokens_file)

# API Endpoints
CLUBHOUSE_CHAT_URL = "https://api.clubhouse.com/get_room_chat"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"
SPOTIFY_ADD_URL = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

# Spotify API credentials (Replace with actual tokens)
SPOTIFY_TOKEN = "YOUR_SPOTIFY_ACCESS_TOKEN"
PLAYLIST_ID = "YOUR_SPOTIFY_PLAYLIST_ID"

# Function to get messages from Clubhouse room chat
def get_clubhouse_messages(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(CLUBHOUSE_CHAT_URL, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json().get("messages", [])
    except requests.RequestException as e:
        print(f"Failed to fetch messages: {e}")
        return []

# Function to search for a song on Spotify
def search_song_on_spotify(song_name):
    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}
    params = {"q": song_name, "type": "track", "limit": 1}
    try:
        response = requests.get(SPOTIFY_SEARCH_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        tracks = response.json().get("tracks", {}).get("items", [])
        return tracks[0]["uri"] if tracks else None
    except requests.RequestException as e:
        print(f"Spotify search failed: {e}")
        return None

# Function to add a song to Spotify playlist
def add_song_to_playlist(song_uri):
    headers = {
        "Authorization": f"Bearer {SPOTIFY_TOKEN}",
        "Content-Type": "application/json"
    }
    data = json.dumps({"uris": [song_uri]})
    try:
        response = requests.post(SPOTIFY_ADD_URL.format(playlist_id=PLAYLIST_ID), headers=headers, data=data, timeout=5)
        response.raise_for_status()
        print("Song added successfully!")
    except requests.RequestException as e:
        print(f"Failed to add song: {e}")

# Function to process messages asynchronously
def process_messages(token):
    messages = get_clubhouse_messages(token)
    for message in messages:
        song_name = message.get("text", "").strip()
        if song_name:
            print(f"Searching for: {song_name}")
            song_uri = search_song_on_spotify(song_name)
            if song_uri:
                add_song_to_playlist(song_uri)
            else:
                print("Song not found on Spotify.")

# Run processing with threading for efficiency
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(process_messages, tokens)

time.sleep(2)  # Allow time for async operations to complete
