from utils.get_year_from_date import get_year_from_date
from utils.list_artists import list_artists
from get_tracks import get_tracks_data
from download_song import download_tracks
from mp4_to_mp3 import mp4_to_mp3
from add_metadata import add_metadata
from utils.recreate_directory import recreate_directory
from utils.album_type import album_type

def main():
    data = get_tracks_data()
    songs= list(reversed(data['items']))
    for item in songs:
        track = item['track']
        song = track['name']
        album = album_type(type = track['album']['album_type'], name=track['album']['name'])
        artist = list_artists(track['artists'])
        year = get_year_from_date(track['album']['release_date'])
        track_num = track['track_number']
        cover = track['album']['images'][0]['url']
        print("\tTrack:")
        print("\t\t" + "Song: ", song)
        print("\t\t" + "Album: ", album)
        print("\t\t" + "Artist: ", artist)
        name = download_tracks(f'{song} - {artist}')
        mp4_to_mp3(name)
        add_metadata(file_name=name, song=song, artist=artist, album=album, track_number=f'{track_num}', year=year, cover=cover)

    recreate_directory()
main()