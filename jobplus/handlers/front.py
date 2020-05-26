from flask import Blueprint, render_template
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@front.route('/userregister')
def userregister():
    form = UserRegisterForm()
    return render_template('userregister.html', form=form)

@front.route('/companyregister')
def companyregister():
    form = CompanyRegisterForm()
    return render_template('companyregister.html', form=form)
