from todo_app.models import Todo,construct
import time

def fetch(list):
    todo_list = Todo.query.all()
    for item in todo_list:
        list.append(construct(item.uuid,item.title,item.complete,str(item.date)))
        

def fetch_completed(list):
    todo_list = Todo.query.filter_by(complete="Completed").all()
    for item in todo_list:
        list.append(construct(item.uuid,item.title,item.complete,time.ctime(item.date)))


def fetch_pending(list):
    todo_list = Todo.query.filter_by(complete="Pending").all()
    for item in todo_list:
        list.append(construct(item.uuid,item.title,item.complete,time.ctime(item.date)))


def fetch_details(todo_title):
    item = Todo.query.filter_by(title=todo_title).first()
    return (construct(item.uuid,item.title,item.complete,time.ctime(item.date)))


def fetch_sorted(list):
    todo_list = Todo.query.order_by(Todo.uuid).all()
    for item in todo_list:
        list.append(construct(item.uuid,item.title,item.complete,time.ctime(item.date)))