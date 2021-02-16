from flask import Blueprint
from todo_app.controllers.todo_controllers import delete_item
from todo_app.models import construct
from db.todo_app.todolist.models import Todo

delete = Blueprint('delete', __name__)

@delete.route("/delete/<string:id_no>", methods=["DELETE"])
def removing(id_no):
    return delete_item(id_no=int(id_no))
    