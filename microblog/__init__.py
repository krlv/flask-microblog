from flask import Flask

def create_app():
    # create the Flask application
    app = Flask(__name__)

    # configure the Flask application
    # TBD

    # a simple route
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
