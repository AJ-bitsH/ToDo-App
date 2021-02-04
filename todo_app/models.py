from todo_app import db

class Todo(db.Model):
    uuid = db.Column(db.String(80),primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.String(20))
    date = db.Column(db.Integer)

def construct(uuid,title,complete,date):
    dict = {}
    dict["uuid"]=(uuid)
    dict["title"]=(title)
    dict["status"]=(complete)
    dict["date"]=(date)
    return dict