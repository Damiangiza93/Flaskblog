from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    submit =SubmitField('Dodaj')