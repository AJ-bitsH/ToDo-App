from todo_app.models import construct
from db.todo_app.todolist.models import Todo


def remove(to_delete_id):
    delete_item = Todo.objects.filter(id=to_delete_id).first()
    response = construct(delete_item.id,delete_item.title,delete_item.complete,delete_item.date)
    delete_item.delete()
    return response
