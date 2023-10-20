import os
import Searcher, VideoTrimmer, ChannelIndexer, EndVideo

if not os.path.exists(os.path.join(os.getcwd(), "videos")):
    os.mkdir(os.path.join(os.getcwd(),"videos"))
if not os.path.exists(os.path.join(os.getcwd(), "videosTrimmed")):
    os.mkdir(os.path.join(os.getcwd(),"videosTrimmed"))

# Searcher.Clear()
# Searcher.Src(input("Input prompt:"), 5) 

# ChannelIndexer.Clear()
# ChannelIndexer.Index(input("Input playlist:"), 10)

# VideoTrimmer.Clear()
# VideoTrimmer.Trim() 

# EndVideo.Combine()