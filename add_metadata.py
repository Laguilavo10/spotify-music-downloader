import eyed3
import os
import urllib.request as request

def add_metadata(file_name, song, artist, album, track_number, year, cover):
    mp3 = eyed3.load(os.getcwd()+'\\'+file_name+'.mp3')
    if (mp3.tag == None):
        mp3.initTag()
    mp3.tag.title = song
    mp3.tag.album = album
    mp3.tag.artist = artist
    # mp3.tag.genre = genre
    mp3.tag.year = year
    mp3.tag.track_num = track_number
    response = request.urlopen(cover)
    imagedata = response.read()
    mp3.tag.images.set(3, imagedata, 'image/png')
    mp3.tag.save(version=eyed3.id3.ID3_V2_3)