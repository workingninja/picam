#!/usr/bin/env python
from flask import Flask, jsonify, render_template, request, Response

from camera.camera import Camera
import ir.ir_control as ir_control


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ir_status')
def ir_status():
    ir_status = ir_control.ir_status()
    return jsonify(ir_status)


@app.route('/ir_switch', methods=['POST'])
def ir_switch():
    value = int(request.form['value'])
    ir_control.ir_switch(value)
    return jsonify({})


@app.route('/video_stream')
def video_stream():
    def gen(camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

