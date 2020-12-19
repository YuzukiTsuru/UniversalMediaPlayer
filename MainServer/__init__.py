from flask import Flask, request
from .Stream import *


def mainApp(config=None, logger=None, file_list=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config is not None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    streamer = Stream(logger)

    # Router
    @app.route('/')
    def _index():
        return 'UniversalMediaPlayer'

    # Streamer

    @app.route('/player_stream', methods=['POST', 'GET'])
    def player_stream():
        return Response(streamer.StreamGen(b''), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/player_main', methods=['POST', 'GET'])
    def player_main():
        if file_list is None:
            return streamer.PartialResponse(request.form.get("file"), 0)
        else:
            play_list_data = request.form.get("file")

    @app.errorhandler(404)
    def page_not_found():
        return 'This page does not exist', 404

    return app
