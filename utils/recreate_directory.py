import os
import shutil
# from utils.config import pathSaveVideos

def recreate_directory():
    if os.path.exists('C:\\Users\\andre\\Music\\Videos-music\\'):
      shutil.rmtree('C:\\Users\\andre\\Music\\Videos-music\\')
      os.mkdir('C:\\Users\\andre\\Music\\Videos-music\\')


