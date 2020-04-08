from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ChoreForm(FlaskForm):
    name = StringField("Chore name", [validators.Length(min=2, max=20)])
    points = IntegerField("Chore points", [validators.NumberRange(min=1, max=1000)])
 
    class Meta:
        csrf = False