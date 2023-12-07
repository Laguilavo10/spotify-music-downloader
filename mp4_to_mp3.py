from moviepy.editor import *
def mp4_to_mp3(name):
    video = VideoFileClip('C:\\Users\\andre\\Music\\Videos-music\\'+name+'.mp4')
    audio = video.audio
    audio.write_audiofile('C:\\Users\\andre\\Music\\Music'+name+'.mp3', logger=None)
    audio.close()
    video.close()
