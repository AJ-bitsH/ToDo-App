from db.todo_app.todolist.models import Todo

def change(to_update_id,change_to):
    item = Todo.objects.filter(id=int(to_update_id)).first()
    item.complete=change_to
    item.save()

    return item
    