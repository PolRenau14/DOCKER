from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/rfm")
    def index():
        return "hello world"
    
    return app
