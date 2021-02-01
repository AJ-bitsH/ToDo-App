from flask import request,Blueprint
from todo_app.models import Todo
from todo_app.database_layer.add_api.add import insert
from todo_app.controllers.todo_controllers import format

add = Blueprint('add', __name__)

@add.route("/add", methods=["POST"])
def addition():
    to_add_title = request.get_json()["title"]
    new_todo = Todo(title=to_add_title, complete= "Pending")
    format(item=new_todo)  #business logic applied
    insert(item=new_todo)  #entry added to db
    return "successfully added item"
