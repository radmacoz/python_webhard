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

    # flask의 migrate 기능이 인식할 수 있도록
    from . import models

    # blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app