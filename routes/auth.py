from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from extensions import db
from models import User
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash('All fields are required', 'danger')
            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(email=email).first()
        
        if existing_user:
            flash('Email already exists', 'danger')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password)
        # Changed user_name to username
        user = User(username=username,
                    email=email,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            # Changed user_name to username
            session['username'] = user.username
            flash('Login successful', 'success')
            return redirect(url_for('notes.dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout successful', 'info')
    return redirect(url_for('auth.login'))