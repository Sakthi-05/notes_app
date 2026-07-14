import os
from flask import Flask,render_template,request
#importing the models to know about the tables and sqlalchemy
from models import User,Note
from extensions import db
from config import config

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    #create the instance folder if it doesnt exist
    os.makedirs(app.instance_path,exist_ok=True)

    try:
        from routes.auth  import auth_bp
        from routes.notes import notes_bp
        from routes.api import api_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(notes_bp)
        app.register_blueprint(api_bp)
    except ImportError:
        pass


    @app.route('/')
    def hello_world():
        return """
    <h1>Hello,World!</h1>
    <p>My notes app</p>
    <p>project setup done 
    and databases connected
    </p>
    """

    with app.app_context():
        db.create_all()

    return app

app=create_app()


# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':
#         username=request.form['username']
#         email=request.form['email']
#         password=request.form['password']

#         user=User(user_name=username,email=email,password=password)
#         db.session.add(user)
#         db.session.commit()
#         return "User registered successfully"
#     return render_template('register.html')

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)