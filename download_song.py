from pytube import YouTube, Search

def download_tracks(song):
    searchedSong = Search(f'{song} letra')
    video_id = searchedSong.results[0].video_id
    yt = YouTube(f'http://youtube.com/watch?v={video_id}')
    yt.streams.get_lowest_resolution().download(output_path='C:\\Users\\andre\\Music\\Videos-music')
    return yt.title
