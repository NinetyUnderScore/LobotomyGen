from pytube import YouTube 
import os
import Searcher
import VideoTrimmer
import ChannelIndexer
import EndVideo

# Searcher.Clear()
Searcher.Src(input("Input prompt:"), 5) 

# ChannelIndexer.Clear()
# ChannelIndexer.Index(input("Input playlist:"), 10)

# VideoTrimmer.Clear()
VideoTrimmer.Trim() 

EndVideo.Combine()