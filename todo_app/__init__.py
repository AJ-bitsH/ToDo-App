from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskext.mysql import MySQL

mysql = MySQL()


db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    from todo_app.database_layer.add_api.add import add
    from todo_app.database_layer.update_api.update import update
    from todo_app.database_layer.delete_api.delete import delete
    from todo_app.database_layer.show_api.show import show
    
    app.register_blueprint(add)
    app.register_blueprint(show)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    

    with app.app_context():
        db.create_all()

    return app

