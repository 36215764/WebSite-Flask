from flask import Blueprint, Flask, json, render_template, request, flash
from flask_login import login_required, current_user
from website.models import Note
from website.ext.database import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-node', methods=['POST'])
@login_required
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']

    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return {}

def init_app(app: Flask):
    app.register_blueprint(views, url_prefix='/')