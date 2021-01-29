# _*_ coding : UTF-8 _*_
#开发人员 ： 纠结中的忐忑
#开发时间 ： 2020/5/26  19:33
#文件名称 ： company.py.PY
#开发工具 ： PyCharm

from flask import Blueprint, render_template, redirect, url_for, flash, request
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from flask_login import login_user, logout_user, login_required, current_user
from jobplus.models import User, CompanyDetail
from jobplus.forms import CompanyEditForm

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter(User.role==User.ROLE_COMPANY).order_by(User.created_at.desc()).paginate(
        page=page, per_page=12, error_out=False
    )
    return render_template('company/index.html', pagination=pagination, active='company')

@company.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('您不是企业用户','warning')
        return redirect(url_for('front.index'))
    form = CompanyEditForm(obj=current_user.company_detail)
    form.name.data = current_user.name
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.update_company(current_user)
        flash('企业信息更新成功','success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)
