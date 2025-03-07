# Spotify Clubhouse Song Request

## Overview
This project integrates **Clubhouse room chats** with **Spotify**, allowing users to request songs in a Clubhouse chat, search for them on Spotify, and automatically add them to a playlist.

## Features
✅ Fetch chat messages from a Clubhouse room where the user is present.  
✅ Extract song requests from user messages.  
✅ Search for songs on **Spotify** using the **Spotify Web API**.  
✅ Automatically add songs to a **Spotify playlist**.  
✅ Multi-threaded execution for efficiency.  

## Requirements
- Python 3.x
- A **Clubhouse API Token** (or authentication workaround)
- A **Spotify API Token** with playlist modification permissions
- `requests` module for API calls
- `concurrent.futures` for multi-threading

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/spotify-clubhouse-song-request.git
   cd spotify-clubhouse-song-request
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Set up **Spotify API Credentials**:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create an app and get the **Access Token**
   - Replace `YOUR_SPOTIFY_ACCESS_TOKEN` and `YOUR_SPOTIFY_PLAYLIST_ID` in the script

4. Set up **Clubhouse Authentication**:
   - Obtain **Clubhouse API Token** (workarounds may be required)
   - Store API tokens in `tokens.txt`, one per line

## Usage
Run the script to process song requests:
```sh
python script.py
```

The script will:
1. Identify the Clubhouse room the user (token) is in.
2. Read chat messages and extract song requests.
3. Search for the song on Spotify.
4. Add the song to the specified Spotify playlist.

## Contributing
Pull requests are welcome! Please open an issue first to discuss changes.

## License
This project is open-source and available under the **MIT License**.

## Disclaimer
This project is for educational purposes. Use Clubhouse API responsibly, as it does not provide an official public API.

