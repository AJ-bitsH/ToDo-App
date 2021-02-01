from todo_app import db
from todo_app.models import Todo

def remove(to_delete_title):
    item = Todo.query.filter_by(title=to_delete_title).first()
    db.session.delete(item)
    db.session.commit()