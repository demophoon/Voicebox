from flask import Flask, jsonify, request

import voicebox
import json

app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/api/move')
def move():
    id = request.args.get('id')
    to = request.args.get('to')
    return jsonify(voicebox.move_in_queue(id, to))

@app.route('/api/queue')
def queue():
    return jsonify(voicebox.get_queue())


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int("8450")
    )
