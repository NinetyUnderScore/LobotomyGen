import VideoGen.Searcher, VideoGen.VideoTrimmer, VideoGen.ChannelIndexer, VideoGen.EndVideo, VideoGen.ProgressLogger
from flask import session

def Handle(cmd, p1, p2, p3):
    if cmd == "clearResults":
        VideoGen.Searcher.Clear()
    
    elif cmd == "clearTrimmed":
        VideoGen.VideoTrimmer.Clear()

    elif cmd == "clearAll":
        VideoGen.Searcher.Clear()
        VideoGen.VideoTrimmer.Clear()
    
    elif cmd == "search":
        VideoGen.Searcher.Src(p1, int(p2))
    
    elif cmd == "playlist":
        VideoGen.ChannelIndexer.Index(p1, int(p2))

    elif cmd == "trim":
        VideoGen.VideoTrimmer.Trim()
    
    elif cmd == "combine":
        VideoGen.EndVideo.Combine()

    elif cmd == "getProgress":
        progress = session.get("progress")

        return { "status": True, 
                 "message": progress }

    elif cmd == "getResults":
        videos = VideoGen.Searcher.Get()

        return {
            "status": True,
            "list": videos
        }
    
    elif cmd == "getTrimmed":
        videos = VideoGen.VideoTrimmer.Get()

        return {
            "status": True,
            "list": videos
        }
    
    else:
        raise Exception("Not a recognized command.")
    
    return {
                    "status": True,
                    "message" : "yipee!",
                    "command" : cmd,
                    "param1" : p1,  
                    "param2" : p2,
                    "param3" : p3
                }