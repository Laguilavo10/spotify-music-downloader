import os 
from dotenv import load_dotenv
load_dotenv('.env')

spotipy_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
pathSaveMusic = os.getenv("PATH_SAVE_MUSIC")
pathSaveVideos = os.getenv("PATH_SAVE_VIDEO_MUSIC")
tracks_count= os.getenv("TRACKS_COUNT")
