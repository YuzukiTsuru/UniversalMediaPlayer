import argparse

from flask import Flask

from MainServer import *
from MPlayer import *

if __name__ == '__main__':
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # create and configure the app
    player = MPlayer(app.logger)

    # run mainApp
    mainApp(app, player, config=Config).run()
