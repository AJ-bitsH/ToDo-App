from todo_app import db
from todo_app.models import Todo

def change(to_update_title):
    item = Todo.query.filter_by(title=to_update_title).first()
    if(item.complete=="Pending"):
        item.complete = "Completed"
    elif(item.complete=="Completed"):
        item.complete = "Pending"
    db.session.commit()