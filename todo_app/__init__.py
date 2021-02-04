from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hortonworks1@localhost/sample_db'
    db.init_app(app)
    

    from todo_app.handlers.add_api.add import add
    from todo_app.handlers.update_api.update import update
    from todo_app.handlers.delete_api.delete import delete
    from todo_app.handlers.show_api.show import show
    
    app.register_blueprint(add)
    app.register_blueprint(show)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    
    with app.app_context():
        db.create_all()

    return app

