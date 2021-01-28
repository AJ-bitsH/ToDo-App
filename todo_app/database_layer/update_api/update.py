from flask import Flask,request,Blueprint
from todo_app import db
from todo_app.models import Todo

update = Blueprint('update', __name__)

@update.route("/update",methods=["PATCH"])
def changing():
    to_update_title = request.get_json()["title"]
    item = Todo.query.filter_by(title=to_update_title).first()
    item.complete = not item.complete
    db.session.commit()
    return "successfully changed state"