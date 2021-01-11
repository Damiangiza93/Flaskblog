from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):                                      # sprawdza czy nie ma już tego usera w bazie danych
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Użytkownik o tej nazwie już istnieje. Wybierz inną nazwę użytkownika.')
    
    def validate_email(self, email):                                      # sprawdza czy nie ma już tego usera w bazie danych
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Użytkownik o tym mailu już istnieje.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj')
    submit = SubmitField('Zaloguj się')


