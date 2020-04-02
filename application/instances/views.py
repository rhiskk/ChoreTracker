from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.instances.models import Instance
from application.chores.models import Chore

@app.route("/instances/<int:chore_id>", methods=["POST"])
@login_required
def instances_create(chore_id):
    
    i=Instance(current_user.id, chore_id)
    gId=Chore.query.get(chore_id).group_id
    db.session().add(i)
    db.session().commit()

    return redirect(url_for("groups_view", group_id=gId))
