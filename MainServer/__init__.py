from flask import request
from .utils import *


def mainApp(app, player, config=None):
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
            require_state = request.args.get("get_state")
            return player.get_state

    return app
