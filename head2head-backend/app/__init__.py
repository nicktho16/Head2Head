from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # register your routes
    from app.routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app