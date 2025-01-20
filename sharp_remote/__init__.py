"""sharp_remote Module"""

# Welcome to the Flask-Bootstrap sample application. This will give you a
# guided tour around creating an application using Flask-Bootstrap.
#
# To run this application yourself, please install its requirements first:
#
#   $ pipenv [ --dev ] install
#
# Then, you can actually run the application.
#
#   $ FLASK_DEBUG=1 FLASK_APP=sharp_remote flask run -h 0.0.0.0
#
# Afterwards, point your browser to http://localhost:5000

import toml
from flask import Flask
from flask_bootstrap import Bootstrap5

from .frontend import frontend
from .api import api

def create_app(config='remote.toml'):
    app = Flask(__name__)
    app.config.from_file(config, load=toml.load)

    # Install our Bootstrap extension
    Bootstrap5(app)

    # Our application uses blueprints as well, register them.
    app.register_blueprint(frontend)
    app.register_blueprint(api)

    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
