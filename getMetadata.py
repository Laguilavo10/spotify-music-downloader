import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config
import spotipy.util as util
import sys

# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
# scope = "user-library-read"
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)
# export SPOTIPY_CLIENT_ID = 'e6b71f14335e42ee9e8d0656adb171d1' 
# export SPOTIPY_CLIENT_SECRET= '66bca6ead5e94e21bd9288971296e07b'
# scope = 'playlist-read-private'
# client_id = config('CLIENT_ID')
# client_secret = config('CLIENT_SECRET')

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# results = sp.current_user_saved_tracks()
# print(results)

scope = 'user-library-read'
token = util.prompt_for_user_token(sys.argv[0],scope,client_id='e6b71f14335e42ee9e8d0656adb171d1',client_secret='66bca6ead5e94e21bd9288971296e07b',redirect_uri='https://google.com')
sp = spotipy.Spotify(auth=token)

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))
results = sp.current_user_saved_tracks()
print(show_tracks(results))