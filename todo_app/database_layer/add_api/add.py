from flask import Flask,request,Blueprint
from todo_app import db
from todo_app.models import Todo

add = Blueprint('add', __name__)

@add.route("/add", methods=["POST"])
def addition():
    to_add_title = request.get_json()["title"]
    new_todo = Todo(title=to_add_title, complete= False)
    db.session.add(new_todo)
    db.session.commit()
    return "successfully added item"