# _*_ coding : UTF-8 _*_
#开发人员 ： 纠结中的忐忑
#开发时间 ： 2020/5/26  19:32
#文件名称 ： user.py.PY
#开发工具 ： PyCharm

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import UserEditForm

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserEditForm(obj=current_user)
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('个人信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('user/profile.html', form=form)