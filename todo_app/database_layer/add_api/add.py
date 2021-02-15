from db.todo_app.todolist.models import Todo

def insert(item):
    Todo.objects.create(title=item.title,complete=item.complete,date=item.date)