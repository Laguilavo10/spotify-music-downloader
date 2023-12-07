from pytube import YouTube, Search
from utils.config import pathSaveVideos

def download_tracks(song):
    searchedSong = Search(f'{song}')
    video_id = searchedSong.results[0].video_id
    yt = YouTube(f'http://youtube.com/watch?v={video_id}')
    yt.streams.get_lowest_resolution().download(output_path=pathSaveVideos)
    return yt.title
