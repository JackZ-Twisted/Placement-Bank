from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This should be secret
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

class LoginForm(FlaskForm):

    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Remember = BooleanField('Remember me')
    # Forgot password text link (Not a form element?)
    # Forgot username text link (Not a form element?)
    Login = SubmitField('Login')
    # Sign up text link (Not a form element?)
    # Login as an employee text link
    # Social media icon links (Not a form element?)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_signup')
def admin_signup():
    return render_template('admin_signup.html')

@app.route('/signup_completion')
def signup_completion():
    return render_template('signup_completion.html')

@app.route('/forgot_username')
def forgot_username():
    return render_template('forgot_username.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')




if __name__ == '__main__':
    app.run(debug=True)