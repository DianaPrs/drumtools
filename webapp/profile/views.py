import json
import re 

from webapp.user.models import User, UserData
from webapp.model import db
from webapp.user.forms import TrackForm

from flask_login import current_user, login_required
from flask import Blueprint, render_template, flash, redirect, url_for, request


blueprint = Blueprint('profile', __name__, url_prefix='/profile')

@blueprint.route("/account")
@login_required
def account():
    title = "Account"
    track_count = UserData.query.filter(UserData.user_id == current_user.id).count()   
    return render_template('profile/account.html', page_title=title, name=current_user.username, track_count=track_count, role=current_user.role, email=current_user.email)

@blueprint.route('/newtrack')
@login_required
def newtrack():
    title = "Create track"
    track_form = TrackForm(user_id=current_user.id)
    return render_template('/profile/newtrack.html', page_title=title,  track_form=track_form)

@blueprint.route('/get_notes', methods=['GET', 'POST'])
def get_notes():
    name = request.form['name']
    pattern = r'<td>(.*?)</td>'     
    match = re.findall(pattern, name)
    list_view = match[::2]
    table_view = json.dumps({'view': list_view}) 
    print(list_view)
    return table_view

@blueprint.route('add_track', methods=['POST'])
def add_track():
    form = TrackForm()
    if form.validate_on_submit():
            track = UserData(artist=form.artist.data, title=form.title.data, comment=form.comment.data, notes=form.notes.data, user_id=current_user.id)
            db.session.add(track)
            db.session.commit()
            flash('Successfully added')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Mistake in field "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))        
    return redirect(request.referrer)   