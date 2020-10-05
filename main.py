import spotipy
from apple_music import pl_fetch 
from apple_music import song_fetch
from spotipy.oauth2 import SpotifyOAuth

#for privacy not including keys
SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI=''

scope = "playlist-modify-public user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

user_id = sp.me()['id']
sp.user_playlist_create(sp.me()['id'], "fake playlist")