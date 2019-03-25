from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from web import NameForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'we11029af102hhlayu801ho1'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("404.html"), 500


@app.route("/form", methods=["GET", "Post"])
def index_form():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        # name = form.name.data
        # form.name.data = ''
        return redirect(url_for("index_form"))
    return render_template("form.html", form=form, name=session.get("name"))


@app.route("/flash", methods=["get", "post"])
def index_flash():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None or old_name != form.name.data:
            flash("Look like you had change your name")
        session["name"] = form.name.data
        return redirect(url_for("index_flash"))
    return render_template("form.html", form=form, name=session.get("name"))


if __name__ == '__main__':
    app.run(debug=True)
