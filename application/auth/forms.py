from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2, max=20)])
    username = StringField("username", [validators.Length(min=3, max=20)])
    password = PasswordField("password", [validators.Length(min=4, max=30)])

    class Meta:
        csrf = False