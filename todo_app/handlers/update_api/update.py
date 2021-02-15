from flask import request,Blueprint
from todo_app.controllers.todo_controllers import update_item
from todo_app.models import construct

update = Blueprint('update', __name__)

@update.route("/update",methods=["PATCH"])
def changing():
    id_no = request.get_json()["title"]
    to_status = request.get_json()["change_to"]
    item = update_item(id_no=id_no,change_to=to_status)
    return construct(item.id,item.title,item.complete,item.date)