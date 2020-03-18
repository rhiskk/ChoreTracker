from application import app, db
from flask import redirect, render_template, request, url_for
from application.chores.models import Chore

@app.route("/chores", methods=["GET"])
def chores_index():
    return render_template("chores/list.html", chores = Chore.query.all())

@app.route("/chores/new/")
def chores_form():
    return render_template("chores/new.html")

@app.route("/chores/<chore_id>/", methods=["POST"])
def chores_change_points(chore_id):

    c = Chore.query.get(chore_id)
    c.points = request.form.get("points")
    db.session().commit()
  
    return redirect(url_for("chores_index"))

@app.route("/chores/", methods=["POST"])
def chores_create():
    c = Chore(request.form.get("name"), request.form.get("points"))

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("chores_index"))