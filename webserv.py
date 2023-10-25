from flask import Flask, jsonify, request, session
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
            data0 = request.form
            
            command = request.form.getlist('command')
            command = command[0] if command else None
            param1 = request.form.getlist('param1')
            param1 = param1[0] if param1 else None
            param2 = request.form.getlist('param2')
            param2 = param2[0] if param2 else None
            param3 = request.form.getlist('param3')
            param3 = param3[0] if param3 else None

            response = jsonify(PostHandler.Handle(command, param1, param2, param3))

            response.message = session.get("progress")

            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as exc:
            response = jsonify({
                    "status": False,
                    "message" : str(exc)
                    })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

if __name__ == '__main__':
    port = 9900
    app.run(host='0.0.0.0', port=port)