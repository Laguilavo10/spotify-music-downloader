import os
import shutil
from utils.config import pathSaveVideos

def recreate_directory():
    if os.path.exists(pathSaveVideos):
      shutil.rmtree(pathSaveVideos)
      os.mkdir(pathSaveVideos)


