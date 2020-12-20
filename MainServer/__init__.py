from flask import Flask, request
from .Stream import *
from .utils import *


def mainApp(config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config is not None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config)

    streamer = Stream(app.logger)

    # Router
    @app.route('/')
    def _index():
        return 'UniversalMediaPlayer'

    @app.route('/controller', methods=['POST', 'GET'])
    def controller():
        return 'UniversalMediaPlayer'

    # Streamer
    @app.route('/player_stream', methods=['POST', 'GET'])
    def player_stream():
        return Response(streamer.StreamGen(b''), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/player_main', methods=['POST', 'GET'])
    def player_main():
        if request.method == 'GET':
            file_path = request.args.get("file")
            if FileExist(file_path):
                return streamer.PartialResponse(file_path)
            else:
                return Response(streamer.StreamGen(b''), mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            pass

    return app
