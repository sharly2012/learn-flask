from datetime import datetime
from flask import render_template, url_for, session, redirect
from app.main import main
from app.main.forms import NameForm


def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"), known=session.get("known", False),
                           current_time=datetime.utcnow())
