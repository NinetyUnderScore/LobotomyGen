from flask import Flask, jsonify, request
import os
import PostHandler

if not os.path.exists(os.path.join(os.getcwd(), "VideoGen/videos")):
    os.mkdir(os.path.join(os.getcwd(),"VideoGen/videos"))
if not os.path.exists(os.path.join(os.getcwd(), "VideoGen/videosTrimmed")):
    os.mkdir(os.path.join(os.getcwd(),"VideoGen/videosTrimmed"))

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def req():
    if request.method == "POST":
        try:
            data = {
                    "status": True,
                    "message" : "yipee!",
                    "received" : request.headers["command"],
                    "param1" : request.headers["param1"],
                    "param2" : request.headers["param2"],
                    "param3" : request.headers["param3"]
                }

            PostHandler.Handle(request.headers["command"], request.headers["param1"], request.headers["param2"], request.headers["param3"])

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