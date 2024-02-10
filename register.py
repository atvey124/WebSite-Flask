from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    email = EmailField("email",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("submit")