import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from study_room.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        type_user = int(request.form.get('type_user'))
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        
        print(first_name)
        print(last_name)
        print(username)
        print(password)
        print(" ****** " + str(type_user))

        if not (first_name and last_name and str(type_user) and username and password):
            error = "Please fill all requiered fields"
    
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (first_name, last_name, type, username, password) VALUES (?, ?, ?, ?, ?)',
                (first_name, last_name, type_user, username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('room.index'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/profile')
def profile():
    return render_template('auth/profile.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

#se valida que el usuario se encuentre logeado.
#Require Authentication in Other Views
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view        