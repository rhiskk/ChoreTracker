from application import app, db
from flask import redirect, render_template, request, url_for
from application.chores.models import Chore
from application.chores.forms import ChoreForm
from application.chores.forms import ChangePointsForm


@app.route("/chores", methods=["GET"])
def chores_index():
    return render_template("chores/list.html", chores=Chore.query.all(), form=ChangePointsForm())


@app.route("/chores/new/")
def chores_form():
    return render_template("chores/new.html", form=ChoreForm())


@app.route("/chores/<chore_id>/", methods=["POST"])
def chores_change_points(chore_id):

    form = ChangePointsForm(request.form)
    if not form.validate():
        return render_template("chores/list.html", chores=Chore.query.all(), form=form)
    c = Chore.query.get(chore_id)
    c.points = form.points.data
    db.session().commit()

    return redirect(url_for("chores_index"))


@app.route("/chores/", methods=["POST"])
def chores_create():
    form = ChoreForm(request.form)

    if not form.validate():
        return render_template("chores/new.html", form=form)

    c = Chore(form.name.data, form.points.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("chores_index"))
