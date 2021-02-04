from flask import Blueprint
from todo_app.database_layer.show_api.show import fetch, fetch_completed, fetch_details, fetch_pending, fetch_sorted
import json

show = Blueprint('show', __name__)

@show.route("/show", methods=["GET"])
def displayingAll():
    list = []
    fetch(list=list)
    return json.dumps(list)

@show.route("/show/completed", methods=["GET"])
def displayingCompleted():
    list = []
    fetch_completed(list=list)
    return json.dumps(list)

@show.route("/show/pending", methods=["GET"])
def displayingPending():
    list = []
    fetch_pending(list=list)
    return json.dumps(list)

@show.route("/show/details/<string:todo_title>", methods=["GET"])
def displayingDetails(todo_title):
    result = fetch_details(todo_title=todo_title)
    return json.dumps(result)

@show.route("/show/urgency", methods=["GET"])
def displayingUrgency():
    list = []
    fetch_sorted(list=list)
    return json.dumps(list)