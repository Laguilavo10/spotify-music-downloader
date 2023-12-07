from moviepy.editor import *
def mp4_to_mp3(name):
    video = VideoFileClip(os.getcwd()+'\\'+name+'.mp4')
    audio = video.audio
    audio.write_audiofile(os.getcwd()+'\\'+name+'.mp3', logger=None)
    audio.close()
    video.close()
