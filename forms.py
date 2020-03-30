from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Benutzername',
                           validators=[DataRequired(message=(u'Bitte geben Sie einen Benutzernamen an')), Length(min=2, max=20, message=(u'Der Benutzername muss zwischen 2-20 Zeichen enthalten.'))])
    email = StringField('E-Mail',
                        validators=[DataRequired(message=(u'Bitte geben Sie eine e-Mail Adresse ein.')), Email(message=(u'Bitte geben Sie eine gültige e-Mail Adresse an.'))])
    password = PasswordField('Passwort', validators=[DataRequired(message=(u'Bitte geben Sie ein Passwort an.'))])
    confirm_password = PasswordField('Passwort bestätigen',
                                     validators=[DataRequired(message=(u'Bitte geben Sie das Passwort erneut ein.')), EqualTo('password', message=(u'Die Passwörter stimmen nicht überein.'))])
    submit = SubmitField('Registrieren')


class LoginForm(FlaskForm):
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Angemeldet bleiben')
    submit = SubmitField('Anmelden')