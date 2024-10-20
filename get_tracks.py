import spotipy
import spotipy.util as util
import sys
from utils.config import spotipy_client_id, spotipy_client_secret, tracks_count, spotipy_redirect_uri, offset_tracks

def get_tracks_data():
    scope = 'user-library-read'
    token = util.prompt_for_user_token(sys.argv[0],scope,client_id=spotipy_client_id,client_secret=spotipy_client_secret,redirect_uri=spotipy_redirect_uri)
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=tracks_count, offset=offset_tracks)
    return results