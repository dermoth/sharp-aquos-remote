"""Flask remote api"""

from flask import Blueprint, json
from .sharp import TvController

api = Blueprint('api', __name__)
mytv = TvController(host='192.168.67.248')  # TODO: allow at least IP connectivity, ideally use ssdp

# Action a remote control key
@api.route('/api/key/<key>', methods=('PUT',))
def handle_key(key):
    """_summary_
    """
    return json.jsonify({'result': 'Hello World'})

@api.route('/api/command/<cmd>/<param>', methods=('PUT',))
def handle_cmd(cmd, param):
    """_summary_
    """
    res = mytv.command(cmd, param)
    return json.jsonify({'result': res})
