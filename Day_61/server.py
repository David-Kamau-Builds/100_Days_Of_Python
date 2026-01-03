from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from config import Config

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Please enter a valid email address.")
        ],
        render_kw={"class": "form-control", "placeholder": "Enter your email"}
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters long.")
        ],
        render_kw={"class": "form-control", "placeholder": "Enter your password"}
    )
    
    submit = SubmitField('Login', render_kw={"class": "btn btn-custom btn-block"})


app = Flask(__name__)

try:
    Config.validate_config()
    app.config.from_object(Config)
except ValueError as e:
    print(f"Configuration Error: {e}")
    exit(1)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if form.email.data == Config.EMAIL and form.password.data == Config.PASSWORD:
            return render_template('success.html'), 200
        else:
            flash('Invalid email or password. Please try again.', 'error')
            return render_template('denied.html'), 401
    
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)