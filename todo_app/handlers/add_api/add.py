from flask import request,Blueprint
from todo_app.models import construct
from db.todo_app.todolist.models import Todo
from todo_app.controllers.todo_controllers import add_item

add = Blueprint('add', __name__)

@add.route("/add", methods=["POST"])
def addition():
    to_add_title = request.get_json()["title"]
    new_todo = Todo(title=to_add_title, complete= "Pending")
    add_item(item=new_todo)
    return construct(new_todo.id,new_todo.title,new_todo.complete,new_todo.date)
