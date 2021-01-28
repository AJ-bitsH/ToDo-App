from todo_app import db

class Todo(db.Model):
    title = db.Column(db.String, primary_key=True)
    complete = db.Column(db.Boolean)