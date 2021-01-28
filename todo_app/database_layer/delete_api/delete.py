from flask import Flask,request,Blueprint
from todo_app import db
from todo_app.models import Todo

delete = Blueprint('delete', __name__)

@delete.route("/delete", methods=["DELETE"])
def removing():
    to_delete_title = request.get_json()["title"]
    item = Todo.query.filter_by(title=to_delete_title).first()
    db.session.delete(item)
    db.session.commit()
    return "succesfully deleted item"