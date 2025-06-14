from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 注册蓝图
    from .routes.hello import hello_bp
    from .routes.organization import api_bp
    app.register_blueprint(hello_bp)
    app.register_blueprint(api_bp)

    return app