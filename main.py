from pytube  import YouTube, Search
import spotipy
import spotipy.util as util
import sys
from moviepy.editor import *
from mp3_tagger import MP3File
import eyed3
import urllib.request as request
# scope = 'user-library-read'
# token = util.prompt_for_user_token(sys.argv[0],scope,client_id='e6b71f14335e42ee9e8d0656adb171d1',client_secret='66bca6ead5e94e21bd9288971296e07b',redirect_uri='https://google.com')
# sp = spotipy.Spotify(auth=token)

import moviepy.editor as mp


#Cargamos el fichero .mp4

# def mp4_to_mp3(name):
#     video = VideoFileClip(os.getcwd()+'\\'+name+'.mp4')
#     audio = video.audio
#     audio.write_audiofile(os.getcwd()+'\\'+name+'.mp3', logger=None)
#     audio.close()
#     video.close()

# mp4_to_mp3('Porfa (Video Oficial)')
# def download_Tracks(song):
#     s = Search(song)
#     video_id = s.results[0].video_id
#     yt = YouTube(f'http://youtube.com/watch?v={video_id}')
#     yt.streams.get_highest_resolution().download()
#     # filter(only_audio=True).last().download(filename=f'{song}.webm')
#     # video = VideoFileClip(os.getcwd()+'\\'+song+'.mp4')
#     # audio = video.audio
#     # audio.write_audiofile(os.getcwd()+'\\'+song+'.mp3', logger=None)
#     # audio.close()
#     # video.close()

# # 
# download_Tracks('porfa feid')

# from pydub import AudioSegment

# def convert_webm_to_mp3(file_name):
#     # print(os.getcwd())
#     file_name = 'hola'
#     audio = AudioSegment.from_file(file_name + '.webm', format='webm')
#     audio.export(file_name + '.mp3', format='mp3')

# convert_webm_to_mp3('porfa feid')
# def show_tracks(results):
#   for item in results['items']:
#     track = item['track']
#     song = f"{track['name']} {track['artists'][0]['name']}"
#     download_Tracks(song)

# results = sp.current_user_saved_tracks()

# print(imagedata)
# # import eyed3
# file = eyed3.load("song.mp3")
# file.tag.images.set(3, imagedata , "image/jpeg" ,u"Description")
# file.tag.save()

def add_metadata(file_name, song, artist, album, track_number, genre, year, cover):
    mp3 = eyed3.load(os.getcwd()+'\\'+file_name+'.mp3')
    if (mp3.tag == None):
        mp3.initTag()
    mp3.tag.title = song
    mp3.tag.album = album
    mp3.tag.artist = artist
    mp3.tag.genre = genre
    mp3.tag.year = year
    mp3.tag.track_num = track_number
    response = request.urlopen(cover)
    imagedata = response.read()
    mp3.tag.images.set(3, imagedata, 'image/png')
    mp3.tag.save(version=eyed3.id3.ID3_V2_3)
  
add_metadata('HIBIKI Bad Bunny', 'Hibiki', 'Bad Bunny', 'nadie saber lo que va a pasar mañana', '4', 'Latin', '2021', 'https://i.scdn.co/image/ab67616d0000b273734b36a0655aae40d78d70f4')



#############
# source env/Scrips/activate