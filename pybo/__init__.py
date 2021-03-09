from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # @app.route('/') # 특정 주소에 접속하면 바로 다음 줄의 함수 호출
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app