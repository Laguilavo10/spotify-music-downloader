from pytube import YouTube, Search

def download_tracks(song):
    searchedSong = Search(song)
    video_id = searchedSong.results[0].video_id
    yt = YouTube(f'http://youtube.com/watch?v={video_id}')
    yt.streams.get_lowest_resolution().download()
    return yt.title

    