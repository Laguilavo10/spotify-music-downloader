from pytube import YouTube, Search
from utils.config import pathSaveVideos
from utils.sanitize_filename import sanitize_filename

def download_tracks(song):
    searchedSong = Search(f'{song} letra')
    video_id = searchedSong.results[0].video_id
    url_video = f'http://youtube.com/watch?v={video_id}'
    print("\t\t" + "Link: ", url_video)
    yt = YouTube(url_video)
    yt.streams.get_lowest_resolution().download(output_path=pathSaveVideos)
    return sanitize_filename(yt.title)
