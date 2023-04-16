"""Flask Frontend server"""
# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

#from flask import Blueprint, render_template, flash, redirect, url_for
from flask import Blueprint, render_template
from flask.logging import default_handler
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
#from markupsafe import escape

from .sharp import TvController
from .nav import nav

frontend = Blueprint('frontend', __name__)
# FIXME: de-duplicate this...
mytv = TvController(host='192.168.67.248')  # TODO: allow at least IP connectivity, ideally use ssdp

# TODO: add a navbar (unfinished)
nav.register_element('frontend_top', Navbar(
    View('Remote', 'frontend'),
))

# The main page shows the remote directly
@frontend.route('/')
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('index.html.j2', mytv=mytv)
