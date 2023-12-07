import spotipy
import spotipy.util as util
import sys

def get_tracks_data():
    scope = 'user-library-read'
    token = util.prompt_for_user_token(sys.argv[0],scope,client_id='e6b71f14335e42ee9e8d0656adb171d1',client_secret='66bca6ead5e94e21bd9288971296e07b',redirect_uri='https://google.com')
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=8)
    return results
