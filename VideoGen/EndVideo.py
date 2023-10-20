import os
import moviepy
import random
import numpy as np
import VideoGen.VideoEffector
from moviepy.editor import vfx, VideoFileClip, CompositeVideoClip

def Combine():
    videos_path = os.path.join(os.path.dirname(__file__),"videosTrimmed")
    Clips = []
    lastTime = 0

    for i,v in enumerate(os.listdir(videos_path)):
        if v.endswith('.mp4'):
            file_path = os.path.join(videos_path, v)
            video = VideoFileClip(file_path)
            
            startTime = lastTime - (int(i!=0) * (1.0 * random.random()))
            video = VideoEffector.Effector(video, startTime, lastTime)
            lastTime = startTime + 3.0
            video = video.set_start(startTime)

            print(str(video) + ": " + str(startTime) + ", " + str(video.duration))

            Clips.append(video)

    

    finalVideo = CompositeVideoClip(Clips)
    finalVideo.write_videofile(os.path.join(os.path.dirname(__file__), "EndVideo.mp4"), codec="libx264", audio_codec="aac", bitrate='50k')


if __name__ == '__main__':
    Combine()