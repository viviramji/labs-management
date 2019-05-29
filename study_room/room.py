from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from werkzeug.exceptions import abort

from study_room.auth import login_required
from study_room.db import get_db

bp = Blueprint('room', __name__)

@bp.route('/')
def index():
    db = get_db()
    rooms = db.execute(
        'SELECT * FROM room'
    ).fetchall()

    return render_template('room/index.html', rooms=rooms)

def get_status(state):
    if state == 1:
        return 0
    else:
        return 1

#get if the room exist
def get_room(id):
    room = get_db().execute(
        'SELECT * FROM room WHERE id = ?',
        (id,)
    ).fetchone()

    if room is None:
        abort(404, "Room id {0} doesn't exist.".format(id))

    return room

@bp.route('/<int:id>/<int:state>/update', methods=('GET', 'POST'))
@login_required
def update(id, state):
    room = get_room(id)
    new_state = get_status(state)
    db = get_db()
    db.execute(
        'UPDATE room SET available = ?', 
        (new_state,)
    )
    db.commit()
    return redirect(url_for('room.index'))

