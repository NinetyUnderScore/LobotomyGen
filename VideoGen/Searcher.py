from pytube import Search
import os

def Src(Query, limit):

    dirname = os.path.dirname(__file__)
    FOLDER = os.path.join(dirname, 'videos/')
    
    s = Search(Query)
    
    count = 0
    for i,v in enumerate(s.results):
        if count >= limit:
            break
        yt = s.results[i]
    
        try:
            stream = yt.streams.get_by_itag(18)
            stream.download(FOLDER)
            count += 1
        except:
            continue
            
        print(str(i)+"/"+str(len(s.results)))
    print("done")

def Clear():
    dirname = os.path.dirname(__file__)
    FOLDER = os.path.join(dirname, 'videos/')

    for i in os.listdir(FOLDER):
        os.remove(os.path.join(FOLDER, i))