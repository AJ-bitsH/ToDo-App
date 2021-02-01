from todo_app.models import Todo
import time

def fetch(list):
    todo_list = Todo.query.all()
    for item in todo_list:
        tuple = {}
        tuple["uuid"]=(item.uuid)
        tuple["title"]=(item.title)
        tuple["status"]=(item.complete)
        tuple["date"]=(time.ctime(item.date))
        list.append(tuple)