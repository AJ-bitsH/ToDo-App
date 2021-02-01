from flask import request,Blueprint
from todo_app.database_layer.update_api.update import change

update = Blueprint('update', __name__)

@update.route("/update",methods=["PATCH"])
def changing():
    item = request.get_json()["title"]
    change(to_update_title=item)
    return "successfully changed state"