from todo_app import db

def insert(item):
    db.session.add(item)
    db.session.commit()