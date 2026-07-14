import os
from flask import Flask, render_template
from models import User, Note
from extensions import db
from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    
    os.makedirs(app.instance_path, exist_ok=True)

    from routes.auth import auth_bp
    from routes.notes import notes_bp
    from routes.api import api_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()
        
    return app

app = create_app()

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)