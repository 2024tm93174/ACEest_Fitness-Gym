from flask import Flask
from .routes import init_routes

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Load test config if provided
    if test_config:
        app.config.update(test_config)
    
    # Initialize all routes
    init_routes(app)
    
    return app
