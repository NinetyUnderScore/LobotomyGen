import VideoGen.Searcher, VideoGen.VideoTrimmer, VideoGen.ChannelIndexer, VideoGen.EndVideo

def Handle(cmd, p1, p2, p3):
    print(cmd)
    if cmd == "clearResults":
        VideoGen.Searcher.Clear()
    
    if cmd == "clearTrimmed":
        VideoGen.VideoTrimmer.Clear()
    
    if cmd == "search":
        VideoGen.Searcher.Src(p1, int(p2))
    
    if cmd == "playlist":
        VideoGen.ChannelIndexer.Index(p1, int(p2))

    if cmd == "trim":
        VideoGen.VideoTrimmer.Trim()
    
    if cmd == "combine":
        VideoGen.EndVideo.Combine()