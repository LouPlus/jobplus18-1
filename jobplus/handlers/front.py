from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from flask_login import login_user, logout_user, login_required
from jobplus.models import User

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        url = 'user.profile'
        if user.is_admin:
            url = 'admin.index'
        elif user.is_company:
            url = 'company.profile'
        return redirect(url_for(url))
    return render_template('login.html', form=form)

@front.route('/userregister', methods=['GET','POST'])
def userregister():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('userregister.html', form=form)

@front.route('/companyregister', methods=['GET','POST'])
def companyregister():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录','success')
    return redirect(url_for('.index'))
