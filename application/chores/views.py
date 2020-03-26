from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.chores.models import Chore
from application.instances.models import Instance
from application.chores.forms import ChoreForm


@app.route("/chores/", methods=["GET"])
def chores_index():
    return render_template("chores/list.html", chores=Chore.query.all())


@app.route("/chores/new/")
@login_required
def chores_form():
    return render_template("chores/new.html", form=ChoreForm())


@app.route("/chores/edit/<int:chore_id>/")
@login_required
def chores_edit_form(chore_id):
    return render_template("chores/edit.html", chore_id=chore_id, chore = Chore.query.get(chore_id), form=ChoreForm())


@app.route("/chores/<int:chore_id>/", methods=["POST"])
@login_required
def chores_edit(chore_id):
    c = Chore.query.get(chore_id)
    form = ChoreForm(request.form)

    if not form.validate():
        return render_template("chores/edit.html", chore_id=chore_id, chore = Chore.query.get(chore_id), form=form)
    c.name = form.name.data
    c.points = form.points.data
    db.session().commit()

    return redirect(url_for("chores_index"))

@app.route("/chores/delete/<int:chore_id>/", methods=["POST"])
@login_required
def chores_delete(chore_id):

    c = Chore.query.get(chore_id)
    Instance.query.filter_by(chore_id = chore_id).delete()
    db.session.delete(c)
    db.session().commit()

    return redirect(url_for("chores_index"))


@app.route("/chores/", methods=["POST"])
@login_required
def chores_create():
    form = ChoreForm(request.form)

    if not form.validate():
        return render_template("chores/new.html", form=form)

    c = Chore(form.name.data, form.points.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("chores_index"))
