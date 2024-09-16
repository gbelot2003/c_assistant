from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.services import check_user_credentials
from app.forms import LoginForm

main = Blueprint('main', __name__)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = check_user_credentials(form.username.data, form.password.data)
        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed. Check username and password', 'danger')
    return render_template('login.html', form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
