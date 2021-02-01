from flask import request,Blueprint
from todo_app.database_layer.delete_api.delete import remove

delete = Blueprint('delete', __name__)

@delete.route("/delete", methods=["DELETE"])
def removing():
    item = request.get_json()["title"]
    remove(to_delete_title=item)
    return "succesfully deleted item"