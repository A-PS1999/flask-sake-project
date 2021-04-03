import os
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import main
from .forms import NewBottleForm
from ..models import User, Bottle


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/collection/<name>')
def collection(name):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    title = user.username

    bottles = Bottle.query.filter_by(user_id=name).all()

    return render_template('collection.html',
                           user=user,
                           title=title,
                           bottles=bottles)


@main.route('/collection/<name>/newbottle', methods=['GET', 'POST'])
@login_required
def update_collection():
    form = NewBottleForm()

    if form.validate_on_submit():
        f = form.photo.data
        fname = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOADS_FOLDER'], fname))

        new_bottle = Bottle(label=form.label.data,
                            identifier=form.identifier.data,
                            photo=fname,
                            category=form.category.data,
                            maker=form.maker.data,
                            status=form.status.data,
                            region=form.region.data,
                            price=form.price.data,
                            user_id=current_user
                            )
        new_bottle.save_bottle()

        return redirect(url_for('collection.html',
                                user=current_user))

    return render_template('new_bottle.html',
                           title='New Bottle',
                           form=form)
