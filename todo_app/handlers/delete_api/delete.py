from flask import request,Blueprint
from todo_app.database_layer.delete_api.delete import remove

delete = Blueprint('delete', __name__)

@delete.route("/delete/<string:todo_title>", methods=["DELETE"])
def removing(todo_title):
    #item = request.get_json()["title"]
    remove(to_delete_title=todo_title)
    return "succesfully deleted item"