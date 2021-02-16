from todo_app.database_layer.delete_api.delete import remove
from todo_app.database_layer.update_api.update import change
from todo_app.database_layer.add_api.add import insert

def add_item(item):
    insert(item=item)
    
def delete_item(id_no):
    return remove(to_delete_id=id_no)

def update_item(id_no,change_to):
    return change(id_no,change_to)

    