import os
import moviepy
import random
import numpy as np
from moviepy.editor import vfx, VideoFileClip, CompositeVideoClip

def Effector(video, startTime, lastTime):
    if (random.random() < 0.5):
        video = video.fx(vfx.mirror_x)
    if (random.random() < 0.125):
        video = video.fx(vfx.invert_colors)  
    
    speed = 1.0 - (random.random()-0.5)
    video = video.fx(vfx.speedx, factor=speed)  

    video = video.fx(vfx.mask_color, color=[255,255,255], thr=10.0)
    
    video = video.subclip(0, video.duration*0.5)
    video = video.crossfadein(lastTime - startTime)
    return video