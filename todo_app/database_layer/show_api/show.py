from todo_app.models import construct
from db.todo_app.todolist.models import Todo
import time

def fetch(list):
    todo_list = Todo.objects.all()
    for item in todo_list:
        list.append(construct(item.id,item.title,item.complete,str(item.date)))
        

def fetch_by_status(list,status):
    todo_list = Todo.objects.filter(complete=status).all()
    for item in todo_list:
        list.append(construct(item.id,item.title,item.complete,str(item.date)))


def fetch_details(todo_title):
    item = Todo.objects.filter(title=todo_title).first()
    return (construct(item.id,item.title,item.complete,str(item.date)))


def fetch_some(list,dict):
    todo_list = Todo.objects.filter(complete=dict["complete"],title=dict["title"])
    for item in todo_list:
        list.append(construct(item.id,item.title,item.complete,time.ctime(item.date)))