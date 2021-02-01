from flask import Blueprint
from todo_app.database_layer.show_api.show import fetch
import json

show = Blueprint('show', __name__)

@show.route("/show", methods=["GET"])
def displaying():
    list = []
    fetch(list=list)
    return json.dumps(list)