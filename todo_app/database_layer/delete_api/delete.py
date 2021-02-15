from db.todo_app.todolist.models import Todo

def remove(to_delete_id):
    delete_item = Todo.objects.filter(id=to_delete_id).first()
    delete_item.delete()
    return delete_item
