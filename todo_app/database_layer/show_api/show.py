from flask import Flask,request,Blueprint
from todo_app import db
from todo_app.models import Todo

show = Blueprint('show', __name__)

@show.route("/show", methods=["GET"])
def dsiplaying():
    todo_list = Todo.query.all()
    dictionary = {}
    for item in todo_list:
        dictionary[item.title] = item.complete
    return dictionary