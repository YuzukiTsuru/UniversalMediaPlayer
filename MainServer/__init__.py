from flask import Flask, request
from .utils import *


def mainApp(config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config is not None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config)

    # Router
    @app.route('/')
    def _index():
        return 'UniversalMediaPlayer'

    @app.route('/controller', methods=['POST', 'GET'])
    def controller():
        if request.method == 'GET':
            require_state = request.args.get("state")

    return app
