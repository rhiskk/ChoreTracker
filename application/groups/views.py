from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.auth.models import User

@app.route("/groups/", methods=["GET"])
def groups_index():
    return render_template("groups/list.html", groups=Group.find_creator_usernames())

@app.route("/usersgroups/", methods=["GET"])
@login_required
def users_groups():
    return render_template("groups/list.html", groups=Group.find_users_groups(current_user.id), users=True)

@app.route("/nonusersgroups/", methods=["GET"])
@login_required
def non_users_groups():
    return render_template("groups/list.html", groups=Group.find_non_users_groups(current_user.id))

@app.route("/groups/new/")
@login_required
def groups_form():
    return render_template("groups/new.html", form=GroupForm())

@app.route("/groups/join/<int:group_id>")
@login_required
def groups_join(group_id):
    g = Group.query.get(group_id)
    g.members.append(current_user)
    db.session().commit()
    
    return redirect(url_for("groups_view", group_id=group_id))

@app.route("/groups/<int:group_id>")
@login_required
def groups_view(group_id):
    g = Group.query.get(group_id)
    c = User.query.get(g.creator_id)
    return render_template("groups/view.html", group=g, creator=c,
                             userPoints=User.count_user_total_points(group_id))

@app.route("/groups/", methods=["POST"])
@login_required
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form=form)

    g = Group(form.name.data, current_user.id)

    db.session().add(g)
    
    g.members.append(current_user)
    db.session().commit()

    return redirect(url_for("users_groups"))
