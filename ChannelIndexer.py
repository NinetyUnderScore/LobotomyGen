from pytube import Playlist
import os

def Index(Query, limit):

    dirname = os.path.dirname(__file__)
    FOLDER = os.path.join(dirname, 'videos/')
    
    c = Playlist(Query)
    
    count = 0
    for i,v in enumerate(c.videos):
        if count >= limit:
            break
        yt = c.videos[i]
    
        try:
            stream = yt.streams.get_by_itag(18)
            stream.download(FOLDER)
            count += 1
        except:
            continue
            
        print(str(i)+"/"+str(len(c.videos)))
    print("done")

def Clear():
    dirname = os.path.dirname(__file__)
    FOLDER = os.path.join(dirname, 'videos/')

    for i in os.listdir(FOLDER):
        os.remove(os.path.join(FOLDER, i))