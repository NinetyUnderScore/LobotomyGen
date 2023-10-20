from flask import Flask, jsonify, request
import os
import VideoGen.Searcher, VideoGen.VideoTrimmer, VideoGen.ChannelIndexer, VideoGen.EndVideo

if not os.path.exists(os.path.join(os.getcwd(), "videos")):
    os.mkdir(os.path.join(os.getcwd(),"videos"))
if not os.path.exists(os.path.join(os.getcwd(), "videosTrimmed")):
    os.mkdir(os.path.join(os.getcwd(),"videosTrimmed"))

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def req():
    if request.method == "POST":
        try:
            data = {
                    "status": True,
                    "message" : "yipee!",
                    "received" : request.headers["command"]
                }

            PostHandler(request.headers["command"])

            return jsonify(data)
        except Exception as exc:
            resp = {
                    "status": False,
                    "message" : str(exc)
                    }
            return jsonify(resp)

if __name__ == '__main__':
    port = 9900
    app.run(host='0.0.0.0', port=port)