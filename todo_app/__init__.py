import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.todo_app.todo_app.settings')
import django
django.setup()
from flask import Flask



def create_app():
    app = Flask(__name__)
    
    

    from todo_app.handlers.add_api.add import add
    from todo_app.handlers.update_api.update import update
    from todo_app.handlers.delete_api.delete import delete
    from todo_app.handlers.show_api.show import show
    
    app.register_blueprint(add)
    app.register_blueprint(show)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    
    

    return app

