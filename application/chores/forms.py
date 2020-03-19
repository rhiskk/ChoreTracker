from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ChoreForm(FlaskForm):
    name = StringField("Chore name", [validators.Length(min=2)])
    points = IntegerField("Chore points")
 
    class Meta:
        csrf = False

class ChangePointsForm(FlaskForm):
    points = IntegerField("Chore points")
 
    class Meta:
        csrf = False