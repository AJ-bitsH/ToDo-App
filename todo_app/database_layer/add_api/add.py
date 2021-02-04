from todo_app import db
from todo_app.models import Todo

def insert(item,to_add_title):
    if(bool(Todo.query.filter_by(title=to_add_title).first())==False):
        db.session.add(item)
        db.session.commit()