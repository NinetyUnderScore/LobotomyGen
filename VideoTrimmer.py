import os
import random
from moviepy.editor import VideoFileClip

def Trim():
    
    FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'videos')
    NEW_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'videosTrimmed')
    
    for file in os.listdir(FOLDER_PATH):
        if file.endswith('.mp4'):
            file_path = os.path.join(FOLDER_PATH, file)
            new_file_path = os.path.join(NEW_FOLDER_PATH, file)
            clip = VideoFileClip(file_path)
            randomTime = random.randint(0,int(clip.duration)-30)
            trimmed_clip = clip.subclip(randomTime, randomTime+30)
            trimmed_clip.write_videofile(new_file_path, codec="libx264", audio_codec="aac")

def Clear():

    FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'videosTrimmed')
    
    for file in os.listdir(FOLDER_PATH):
        if file.endswith('.mp4'):
            file_path = os.path.join(FOLDER_PATH, file)
            os.remove(file_path)