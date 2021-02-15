from flask import Blueprint,request
from todo_app.database_layer.show_api.show import fetch, fetch_by_status, fetch_details, fetch_some
import json

show = Blueprint('show', __name__)

#to display use of single route to have multiple functionalities
@show.route("/show/<string:status>", methods=["GET"])
def displayingCompleted(status):
    list = []
    fetch_by_status(list=list,status=status)
    return json.dumps(list)

@show.route("/show", methods=["GET"])
def displayingAll():
    list = []
    fetch(list=list)
    return json.dumps(list)

@show.route("/show/details/<todo_title>", methods=["GET"])
def displayingDetails(todo_title):
    result = fetch_details(todo_title=request.view_args['todo_title'])
    return json.dumps(result)


@show.route("/show", methods=["GET"])
def displayingSome():
    list = []
    args = request.args
    dict = {}
    for k,v in args.items():
        dict[k]=v
    fetch_some(list,dict)
    return json.dumps(list)